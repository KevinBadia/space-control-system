import threading
import time


class SimulationRunner:
    def __init__(self, step_fn, dt: float = 0.1):
        self.step_fn = step_fn
        self.dt = dt
        self._thread = None
        self._running = False
        self._paused = False

    def start(self):
        if self._running:
            return

        self._running = True
        self._paused = False
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def _run_loop(self):
        while self._running:
            if not self._paused:
                self.step_fn(self.dt)
            time.sleep(self.dt)

    def pause(self):
        self._paused = True

    def resume(self):
        self._paused = False

    def stop(self):
        self._running = False
        self._paused = False
        if self._thread:
            self._thread.join(timeout=1)
            self._thread = None

    def is_running(self):
        return self._running

    def is_paused(self):
        return self._paused
