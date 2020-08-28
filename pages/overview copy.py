import dash
import pickle
import copy
import pathlib
import math
import datetime as dt
import pandas as pd
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import utils
import plotly.graph_objects as go

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

# Load data
df = pd.read_csv(DATA_PATH.joinpath("Data Science Bootcamp Data_2.0.csv"))
df_cluster = pd.read_csv(DATA_PATH.joinpath("ClusterData.csv"))

fig = go.Figure()
fig.add_trace(go.Histogram(
    x = df_cluster['No of Years'][df_cluster['Gender'] == 'Male'],
    name='Male',
    xbins=dict(
        start = 0,
        end = 60,
        size = 5
    ),
    marker_color='#EB89B5',
    opacity=0.75
))

fig.add_trace(go.Histogram(
    x=df_cluster['No of Years'][df_cluster['Gender'] == 'Female'],
    name='Female',
    xbins=dict(
        start=0,
        end=60,
        size=5
    ),
    marker_color='#330C73',
    opacity=0.75
))

fig.update_layout(
    title_text='Sampled Results', # title of plot
    xaxis_title_text='Age', # xaxis label
    yaxis_title_text='Count', # yaxis label
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1 # gap between bars of the same location coordinates
)


def create_layout(app):
    # Page layouts
    return html.Div(
    [
        html.Div([utils.Header(app)]),

        #page 1
        html.Div(
            [
                html.Div([utils.get_header(app)]),
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id="main_graph",figure=fig)],
                            className="pretty_container seven columns",
                        ),
                        
                    ],
                    className="row flex-display",
                ),
            ]
        )
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"},
)