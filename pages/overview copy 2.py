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
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H3(
                                        "Bank Customer Segmentation",
                                        style={"margin-buttom": "0px"},
                                    ),
                                ]
                            )
                        ],
                        className="",
                        id="title"
                    ),

                ],
                id="header",
                className="",
                style={"margin-bottom": "25px"},
            ),
            html.Div(
                [
                    html.Div(id='manhattan-control-tabs', className='control-tabs', children=[


                    dcc.Tabs(id='manhattan-tabs', value='what-is', children=[
                dcc.Tab(
                    label='About',
                    value='what-is',
                    children=html.Div(className='control-tab', children=[
                        html.H4(className='what-is', children='What is Manhattan Plot?'),
                        html.P('ManhattanPlot allows you to visualize genome-'
                               'wide association studies (GWAS) efficiently. '
                               'Using WebGL under the hood, you can interactively '
                               'explore overviews of massive datasets comprising '
                               'hundreds of thousands of points at once, or '
                               'take a closer look at a small subset of your data.'),
                        html.P('You can adjust the threshold level and the '
                               'suggestive line in the "Graph" tab.')
                    ])
                ),
                dcc.Tab(
                    label='About2',
                    value='what-is2',
                    children=html.Div(className='control-tab', children=[
                        html.H4(className='what-is2', children='What is Manhattan Plot?'),
                        html.P('ManhattanPlot allows you to visualize genome-'
                               'wide association studies (GWAS) efficiently. '
                               'Using WebGL under the hood, you can interactively '
                               'explore overviews of massive datasets comprising '
                               'hundreds of thousands of points at once, or '
                               'take a closer look at a small subset of your data.'),
                        html.P('You can adjust the threshold level and the '
                               'suggestive line in the "Graph" tab.')
                    ])
                ),
                dcc.Tab(
                    label='About3',
                    value='what-is3',
                    children=html.Div(className='control-tab', children=[
                        html.H4(className='what-is3', children='What is Manhattan Plot?'),
                        html.P('ManhattanPlot allows you to visualize genome-'
                               'wide association studies (GWAS) efficiently. '
                               'Using WebGL under the hood, you can interactively '
                               'explore overviews of massive datasets comprising '
                               'hundreds of thousands of points at once, or '
                               'take a closer look at a small subset of your data.'),
                        html.P('You can adjust the threshold level and the '
                               'suggestive line in the "Graph" tab.')
                    ])
                ),
                dcc.Tab(
                    label='Graph',
                    value='graph',
                    children=html.Div(className='control-tab', children=[
                        html.Div(className='app-controls-block', children=[
                            html.Div(
                                className='app-controls-name',
                                children=[
                                    'Threshold value (red)'
                                ]
                            ),
                            dcc.Slider(
                                id='mhp-slider-genome',
                                className='control-slider',
                                vertical=False,
                                updatemode='mouseup',
                                max=4,
                                min=1,
                                value=2,
                                marks={
                                    i + 1: '{}'.format(i + 1)
                                    for i in range(4)
                                },
                                step=0.05
                            ),
                        ]),
                        html.Div(
                            className='app-controls-block', children=[
                                html.Div(
                                    className='app-controls-name',
                                    children=[
                                        'Suggestive line (purple)',
                                    ]
                                ),
                                dcc.Slider(
                                    id='mhp-slider-indic',
                                    className='control-slider',
                                    vertical=False,
                                    updatemode='mouseup',
                                    max=4,
                                    min=1,
                                    value=3,
                                    marks={
                                        i + 1: '{}'.format(i + 1)
                                        for i in range(4)
                                    },
                                    step=0.05
                                )
                            ]
                        )
                    ])
                )
            ]),

            ]),




                    html.Div(
                        [
                            html.Div(
                                    [html.H6(id="well_text"), html.P("No. of Wells")],
                                    id="wells",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="gasText"), html.P("Gas")],
                                    id="gas",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="oilText"), html.P("Oil")],
                                    id="oil",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="waterText"), html.P("Water")],
                                    id="water",
                                    className="mini_container",
                                ), 
                        ],
                        id="info-container",
                        className="row container-display",
                    )
                ]
            )
        ]
    )