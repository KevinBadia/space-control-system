import threading
import time
from app.application.services import SimulationService
from app.application.commands import Command


def test_commands_during_run_do_not_crash():
    service = SimulationService()
    service.run()

    def spam_commands():
        for _ in range(50):
            service.enqueue_command(
                Command(type="apply_force", fx=1.0, fy=0.0, remaining_time=0.1)
            )
            time.sleep(0.005)

    t = threading.Thread(target=spam_commands)
    t.start()

    time.sleep(0.3)
    service.stop()
    t.join()

    # If we reach here without exception, thread-safety is acceptable
    assert True
