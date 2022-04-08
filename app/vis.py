import altair as alt


def make_vis(df, x_axis: str, y_axis: str, target: str):
    title = f"Monster {x_axis.title()} by {y_axis.title()}"
    text_color = "#AAA"
    graph_color = "#333"
    graph_bg = "#252525"
    graph = alt.Chart(df, title=title).mark_circle(size=100).encode(
        x=x_axis,
        y=y_axis,
        color=target,
        tooltip=alt.Tooltip(list(df.columns)),
    ).properties(
        width=400,
        height=420,
        background=graph_bg,
        padding=40,
    ).configure(
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
            "stroke": graph_color,
        },
    )
    return graph
