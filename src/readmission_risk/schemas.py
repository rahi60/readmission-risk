from typing import Literal

from pydantic import BaseModel, Field


class PatientRecord(BaseModel):
    """One (fictional) discharged patient."""

    age: int = Field(ge=18, le=110)
    sex: Literal["F", "M"]
    systolic_bp: float = Field(ge=60, le=260)
    hba1c: float = Field(ge=3.0, le=20.0)
    prior_admissions: int = Field(ge=0, le=50)
    smoker: bool
