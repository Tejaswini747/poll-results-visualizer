# src/visualization.py

import plotly.express as px

def bar_chart(df):
    fig = px.bar(
        df,
        x="Preferred Tool",
        color="Preferred Tool",
        title="Tool Preference"
    )
    return fig


def pie_chart(df):
    fig = px.pie(
        df,
        names="Preferred Tool",
        title="Tool Share",
        hole=0.4
    )
    return fig


def line_chart(df):
    fig = px.line(
        df.reset_index(),
        y="Satisfaction",
        title="Satisfaction Trend"
    )
    return fig