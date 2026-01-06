from fastapi import APIRouter, HTTPException
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


@router.post("/command")
def command(req: CommandRequest):
    # try:
    #    simulation.apply_command(req.model_dump())
    #    return {"accepted": True}
    #except ValueError as e:
    #    raise HTTPException(status_code=400, detail=str(e))
    if req.type == "reset":
        simulation.__init__()
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