from pydantic import BaseModel


class Scatter(BaseModel):
    x_axis: str = "health"
    y_axis: str = "energy"
    target: str = "rarity"


class Bar(BaseModel):
    x_axis: str = "type"
    target: str = "rarity"


class Pie(BaseModel):
    target: str = "rarity"
