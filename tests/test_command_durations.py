from app.application.services import SimulationService
from app.application.commands import Command


def test_short_duration_command_scales_effect():
    service = SimulationService()

    # mass=1.0 in service by default
    cmd = Command(type="apply_force", fx=10.0, fy=0.0, remaining_time=0.2)
    service.enqueue_command(cmd)

    service.step(1.0)

    # average fx should be 10 * 0.2 / 1.0 = 2.0
    # ax=2.0, dt=1.0 => vx=2.0
    assert abs(service.system.state.vx - 2.0) < 1e-6


def test_overlapping_commands_sum_effects():
    service = SimulationService()

    service.enqueue_command(Command(type="apply_force", fx=4.0, fy=0.0, remaining_time=1.0))
    service.enqueue_command(Command(type="apply_force", fx=6.0, fy=0.0, remaining_time=1.0))

    service.step(1.0)

    # total fx = 10 over full dt => vx should increase by 10
    assert abs(service.system.state.vx - 10.0) < 1e-6


def test_long_command_persists_with_remaining_time():
    service = SimulationService()

    service.enqueue_command(Command(type="apply_force", fx=1.0, fy=0.0, remaining_time=2.5))

    service.step(1.0)
    assert len(service.command_queue) == 1
    assert abs(service.command_queue[0].remaining_time - 1.5) < 1e-6
