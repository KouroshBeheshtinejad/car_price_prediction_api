from pydantic import BaseModel, Field
from typing import Literal

class CarFeatures(BaseModel):
    Make: str
    Year: int = Field(..., ge=1990, le=2025)
    Engine_HP: float       
    Engine_Cylinders: float
    Transmission_Type: Literal['Automatic', 'Manual', 'Semi-Automatic']
    Driven_Wheels: Literal['front', 'rear', 'all']
    Vehicle_Size: Literal['Compact', 'Midsize', 'Large']
    Vehicle_Style: str
    Number_of_Doors: float = Field(..., ge=2, le=5)
    avg_mpg: float
