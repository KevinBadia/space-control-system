from .state import State

class SpacecraftSystem:
    def __init__(self, initial_state: State):
        self.state = initial_state

    def step(self, dt: float):
        """
        Advance the system state by dt.
        Simulation logic will be implemented later.
        """
        pass