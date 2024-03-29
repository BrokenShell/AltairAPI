import altair as alt
from pandas import DataFrame


class Altair:
    text_color = "#AAAAAA"
    graph_color = "#333333"
    graph_bg = "#252525"
    configuration = dict(
        legend={
            "titleColor": text_color,
            "labelColor": text_color,
            "padding": 10,
        },
        title={
            "color": text_color,
            "fontSize": 26,
            "offset": 30,
        },
        axis={
            "titlePadding": 20,
            "titleColor": text_color,
            "labelPadding": 5,
            "labelColor": text_color,
            "gridColor": graph_color,
            "tickColor": graph_color,
            "tickSize": 10,
        },
        view={
            "stroke": graph_bg,
        },
    )
    properties = dict(
        width=400,
        height=420,
        padding=40,
        background=graph_bg,
    )

    def scatter_plot(self, df: DataFrame, x: str, y: str, z: str):
        title = f"Monster {z.title()}: {x.title()} by {y.title()}"
        return alt.Chart(df, title=title).mark_circle(size=100).encode(
            x=alt.X(x, title=x.title()),
            y=alt.Y(y, title=y.title()),
            color=alt.Color(z, title=z.title()),
            tooltip=alt.Tooltip(list(df.columns)),
        ).properties(**self.properties).configure(**self.configuration)

    def bar_graph(self, df: DataFrame, x: str, target: str):
        title = f"Monster {target.title()}: {x.title()} by Count"
        return alt.Chart(df, title=title).mark_bar().encode(
            x=alt.X(x, title=x.title()),
            y=alt.Y("count()", title="Count"),
            color=alt.Color(target, title=target.title()),
            tooltip=alt.Tooltip(list(df.columns)),
        ).properties(**self.properties).configure(**self.configuration)

    def pie_chart(self, df: DataFrame, target: str):
        title = f"Monster {target.title()} Distribution"
        return alt.Chart(df, title=title).mark_arc(innerRadius=80).encode(
            color=alt.Color(target, title=target.title()),
            theta=alt.Theta("count()", title="Count"),
            tooltip=alt.Tooltip(list(df.columns)),
        ).properties(**self.properties).configure(**self.configuration)
