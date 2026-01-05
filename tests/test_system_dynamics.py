from app.domain.state import State
from app.domain.system import SpacecraftSystem


def test_step_with_no_forces_keeps_velocity_constant():
    state = State(
        t=0.0,
        x=0.0,
        y=0.0,
        vx=1.0,
        vy=0.0,
        theta=0.0,
        omega=0.0
    )

    system = SpacecraftSystem(
        initial_state=state,
        mass=1.0,
        inertia=1.0
    )

    system.step(dt=1.0)

    assert state.x == 1.0
    assert state.vx == 1.0
    assert state.t == 1.0


def test_step_with_force_changes_velocity():
    state = State(
        t=0.0,
        x=0.0,
        y=0.0,
        vx=0.0,
        vy=0.0,
        theta=0.0,
        omega=0.0
    )

    system = SpacecraftSystem(
        initial_state=state,
        mass=2.0,
        inertia=1.0
    )

    system.apply_force(fx=2.0, fy=0.0)
    system.step(dt=1.0)

    # ax = fx / m = 1.0
    assert state.vx == 1.0
    assert state.x == 1.0
