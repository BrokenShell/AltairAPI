import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.data import MongoDB
from app.graphs import Altair
from app.types import Pie, Bar, Scatter

API = FastAPI(
    title="Data Science Visualization API",
    version="0.2.1",
    docs_url="/",
    description="<h2>Altair Graphs</h2>",
)
API.mongo = MongoDB()
API.graphs = Altair()
API.add_middleware(
    CORSMiddleware,
    allow_origins=["visfromapi-dev.us-east-1.elasticbeanstalk.com/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@API.get("/version")
async def version():
    return API.version


@API.post("/graphs/scatter-plot")
async def scatter_chart(body: Scatter):
    return {
        "graph": json.loads(API.graphs.scatter_plot(
            df=API.mongo.dataframe(),
            x=body.x_axis,
            y=body.y_axis,
            z=body.target,
        ).to_json()),
        "text": f"This is a scatter plot. It plots monster {body.y_axis} by "
                f"{body.x_axis} for {body.target}."
    }


@API.post("/graphs/bar-graph")
async def bar_graph(body: Bar):
    return {
        "graph": json.loads(API.graphs.bar_graph(
            df=API.mongo.dataframe(),
            x=body.x_axis,
            target=body.target,
        ).to_json()),
        "text": f"This is a stacked bar graph. It graphs monster {body.x_axis} "
                f"for {body.target}.",
    }


@API.post("/graphs/pie-chart")
async def pie_chart(body: Pie):
    return {
        "graph": json.loads(API.graphs.pie_chart(
            df=API.mongo.dataframe(),
            target=body.target,
        ).to_json()),
        "text": f"This is a pie chart. It charts the count of monster "
                f"{body.target}.",
    }
