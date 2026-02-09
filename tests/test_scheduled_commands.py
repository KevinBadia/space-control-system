from app.application.services import SimulationService
from app.application.commands import Command


def test_scheduled_command_does_not_apply_before_start():
    service = SimulationService(load_from_db=False)

    service.enqueue_command(
        Command(type="apply_force", fx=10.0, fy=0.0, remaining_time=2.0, start_at=5.0)
    )

    # advance to t=4 -> should not apply
    service.step(4.0)
    vx_before = service.system.state.vx

    # step to cross start time -> should apply during this step (at least partially)
    service.step(1.0)
    vx_after = service.system.state.vx

    assert vx_after > vx_before
