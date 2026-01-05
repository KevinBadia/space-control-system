from pydantic import BaseModel

class State(BaseModel):
    t: float
    x: float
    y: float
    vx: float
    vy: float
    theta: float
    omega: float