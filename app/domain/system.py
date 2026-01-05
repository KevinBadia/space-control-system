from .state import State

class SpacecraftSystem:
    def __init__(
        self, 
        initial_state: State,
        mass: float,
        inertia: float
    ):
        if mass <= 0 or inertia <= 0:
            raise ValueError("Mass and Inertia must be positive")

        self.state = initial_state
        self.mass = mass
        self.inertia = inertia

        # Control inputs (active during current step)
        self.fx = 0.0
        self.fy = 0.0
        self.torque = 0.0

    def apply_force(self, fx: float, fy: float):
        self.fx = fx
        self.fy = fy

    def apply_torque(self, torque:float):
        self.torque = torque

    def step(self, dt: float):
        if dt <= 0:
            raise ValueError("dt must be positive")

        s = self.state

        # Linear acceleration
        ax = self.fx / self.mass
        ay = self.fy / self.mass

        # Angular acceleration
        alpha = self.torque / self.inertia

        # Update velocities
        s.vx += ax * dt
        s.vy += ay * dt
        s.omega += alpha * dt

        # Update positions
        s.x += s.vx * dt
        s.y += s.vy * dt
        s.theta += s.omega * dt

        # Update time
        s.t += dt

        # Reset control inputs
        self.fx = 0.0
        self.fy = 0.0
        self.torque = 0.0