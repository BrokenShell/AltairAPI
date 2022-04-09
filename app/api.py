import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.data import MongoDB
from app.types import Selections
from app.vis import make_vis

API = FastAPI(
    title="Data Science Visualization API",
    version="0.0.1",
    docs_url="/",
    description="<h2>Full Description</h2>",
)
API.mongo = MongoDB()
API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@API.post("/graph")
async def graph(body: Selections):
    return json.loads(make_vis(
        df=API.mongo.dataframe(body.query),
        x_axis=body.x_axis,
        y_axis=body.y_axis,
        target=body.target,
    ).to_json())
