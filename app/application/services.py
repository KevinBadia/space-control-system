from app.domain.state import State
from app.domain.system import SpacecraftSystem
from app.application.commands import Command
from app.infrastructure.runner import SimulationRunner

import threading 
# No importamos CommandRequest, dado que pasaremos un dict a la función directamente

class SimulationService:
    def __init__(self):
        initial_state = State(
            t=0.0,
            x=0.0,
            y=0.0,
            vx=0.0,
            vy=0.0,
            theta=0.0,
            omega=0.0,
        )

        self.system = SpacecraftSystem(
            initial_state=initial_state,
            mass=1.0,
            inertia=1.0,
        )

        self.history: list[State] = []

        self.command_queue: list[Command] = []

        self.runner = SimulationRunner(self.step, dt=0.1)

        self._lock = threading.Lock()

    def run(self):
        with self._lock:
            self.runner.start()

    def pause(self):
        with self._lock:
            self.runner.pause()

    def resume(self):
        with self._lock:
            self.runner.resume()

    def stop(self):
        with self._lock:
            self.runner.stop()

    def reset(self):
        with self._lock:
            self.runner.stop()
            self.__init__()

    def step(self, dt: float):
#        self.system.step(dt)
#        self.history.append(self.system.state.model_copy())
        """ if dt <= 0:
            raise ValueError("dt must be positive")
        
        # Aggregate active effects
        fx = fy = torque = 0.0

        remaining_commands = []

        for cmd in self.command_queue:
            applied_dt = min(dt, cmd.remaining_time)

            if cmd.type == "apply_force":
                fx += cmd.fx
                fy += cmd.fy

            elif cmd.type == "apply_torque":
                torque += cmd.torque

            cmd.remaining_time -= applied_dt

            if cmd.remaining_time > 0:
                remaining_commands.append(cmd)

        self.command_queue = remaining_commands

        # Apply aggregated effects to domain
        self.system.apply_force(fx, fy)
        self.system.apply_torque(torque)

        self.system.step(dt)
        self.history.append(self.system.state.model_copy()) """

        if dt <= 0:
            raise ValueError("dt must be positive")
        
        with self._lock:
            fx_time = 0.0
            fy_time = 0.0
            torque_time = 0.0
            remaining_commands: list[Command] = []

            for cmd in self.command_queue:
                applied_dt = min(dt, cmd.remaining_time)

                if cmd.type == "apply_force":
                    fx_time += cmd.fx * applied_dt
                    fy_time += cmd.fy * applied_dt

                elif cmd.type == "apply_torque":
                    torque_time += cmd.torque * applied_dt

                cmd.remaining_time -= applied_dt

                if cmd.remaining_time > 0:
                    remaining_commands.append(cmd)

            self.command_queue = remaining_commands

            # Convert time-integrated effects into average inputs over dt
            fx = fx_time / dt
            fy = fy_time / dt
            torque = torque_time / dt

            self.system.apply_force(fx, fy)
            self.system.apply_torque(torque)

            self.system.step(dt)
            self.history.append(self.system.state.model_copy())

    def get_state(self) -> State:
        with self._lock:
            return self.system.state.model_copy()

    def get_history(self, limit: int = 100) -> list[State]:
        with self._lock:
            return self.history[-limit:]

    def get_runtime_status(self):
        with self._lock:
            return {
                "running": self.runner.is_running(),
                "paused": self.runner.is_paused(),
                "dt": self.runner.dt,
                "queue_length": len(self.command_queue),
                "history_size": len(self.history),
                "t": self.system.state.t,
            }


    def apply_command(self, cmd: dict):
        cmd_type = cmd["type"]

        if cmd_type == "apply_force":
            fx = cmd.get("fx", 0.0)
            fy = cmd.get("fy", 0.0)
            self.system.apply_force(fx=fx, fy=fy)
        
        elif cmd_type == "apply_torque":
            torque = cmd.get("torque", 0.0)
            self.system.apply_torque(torque=torque)

        elif cmd_type == "reset":
            self.__init__() # Simple reset for now

        else:
            raise ValueError("Unknown command type")
        
    def enqueue_command(self, cmd: Command):
        if cmd.remaining_time <= 0:
            raise ValueError("Command duration must be positive")

        with self._lock:
            self.command_queue.append(cmd)