from fastapi import APIRouter, HTTPException
from app.application.services import SimulationService
from app.api.schemas import StepRequest, CommandRequest

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
    try:
        simulation.apply_command(req.model_dump())
        return {"accepted": True}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))