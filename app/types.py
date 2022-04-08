from typing import Dict, Optional

from pydantic import BaseModel


class Selections(BaseModel):
    x_axis: str = "health"
    y_axis: str = "energy"
    target: str = "rarity"
    query: Optional[Dict]
