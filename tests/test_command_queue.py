from app.domain.state import State
from app.application.services import SimulationService
from app.application.commands import Command


def test_command_persists_across_steps():
    service = SimulationService()

    cmd = Command(
        type="apply_force",
        fx=1.0,
        fy=0.0,
        remaining_time=2.0,
    )

    service.enqueue_command(cmd)

    service.step(1.0)
    vx_after_first = service.system.state.vx

    service.step(1.0)
    vx_after_second = service.system.state.vx

    assert vx_after_second > vx_after_first
