from app.domain.state import State
from app.domain.system import SpacecraftSystem
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
    
    def step(self, dt: float):
        self.system.step(dt)
        self.history.append(self.system.state.model_copy())

    def get_state(self) -> State:
        return self.system.state

    def get_history(self, limit: int = 100) -> list[State]:
        return self.history[-limit:]

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