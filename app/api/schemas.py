from pydantic import BaseModel, Field
from typing import Literal, Optional


class StepRequest(BaseModel):
    dt: float = Field(gt = 0, le = 10, description= "Time step in seconds")

class CommandRequest(BaseModel):
    type: Literal["apply_force", "apply_torque", "reset"]

    fx: Optional[float] = Field(default = None, ge = -10, le = 10)
    fy: Optional[float] = Field(default = None, ge = -10, le = 10)

    torque: Optional[float] = Field(default = None, ge = -5, le = 5)
    duration: Optional[float] = Field(default=None, gt=0)