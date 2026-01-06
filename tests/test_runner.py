import time
from app.application.services import SimulationService


def test_runner_advances_time():
    service = SimulationService()
    service.run()

    time.sleep(0.3)
    service.pause()

    t_after = service.system.state.t
    assert t_after > 0.0

    service.stop()
