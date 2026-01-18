from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse
from app.application.services import SimulationService
from app.api.schemas import StepRequest, CommandRequest
from app.application.commands import Command

router = APIRouter()
simulation = SimulationService()


@router.get("/state")
def get_state():
    return simulation.get_state()


@router.get("/history")
def get_history(limit: int = 100):
    return simulation.get_history(limit = limit)


@router.post("/step")
def step(req: StepRequest):
    simulation.step(dt=req.dt)
    return {"ok": True, "state": simulation.get_state()}


@router.post("/run")
def run():
    simulation.run()
    return {"running": True}


@router.post("/pause")
def pause():
    simulation.pause()
    return {"paused": True}


@router.post("/resume")
def resume():
    simulation.resume()
    return {"paused": False}


@router.post("/stop")
def stop():
    simulation.stop()
    return {"running": False}

#@router.get("/status")
#def status():
#    return simulation.get_runtime_status()
@router.get("/status")
def status():
    return simulation.get_status()


@router.get("/telemetry")
def telemetry(limit: int = 100):
    # returns last persisted rows
    return simulation.telemetry_repo.fetch_last(limit=limit)

@router.get("/telemetry/export")
def export_telemetry(limit: int = 1000, format: str = "csv"):
    rows = simulation.telemetry_repo.fetch_last(limit=limit)
    rows = list(reversed(rows))  # oldest -> newest

    if format == "json":
        return rows

    # CSV (default)
    if not rows:
        return PlainTextResponse("", media_type="text/csv")

    headers = rows[0].keys()
    lines = [",".join(headers)]
    for r in rows:
        lines.append(",".join(str(r[h]) for h in headers))

    return PlainTextResponse("\n".join(lines), media_type="text/csv")

@router.post("/command")
def command(req: CommandRequest):
    # try:
    #    simulation.apply_command(req.model_dump())
    #    return {"accepted": True}
    #except ValueError as e:
    #    raise HTTPException(status_code=400, detail=str(e))
    if req.type == "reset":
        simulation.reset()
        return {"accepted": True}
    
    duration = req.duration or 1.0

    cmd = Command(
        type=req.type,
        fx=req.fx or 0.0,
        fy=req.fy or 0.0,
        torque=req.torque or 0.0,
        remaining_time=duration,
    )

    simulation.enqueue_command(cmd)
    return {"accepted": True}