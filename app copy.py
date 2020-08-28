# Import required libraries
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

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server


# Load data
df = pd.read_csv(DATA_PATH.joinpath("Data Science Bootcamp Data_2.0.csv"))
df_cluster = pd.read_csv(DATA_PATH.joinpath("ClusterData.csv"))

# Create app layout
app.layout = html.Div(
    [
         html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "Bank Customer Segmentation",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Overview", style={"margin-top": "0px"}
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
         ),
         html.Div(
             [
                 html.Div(
                     [
                         html.Div(
                             [
                                 html.Div(
                                     [html.H6(id="well_text"), html.P("No. of Wells")],
                                     id="wells",
                                     className="mini_container",
                                 ),
                             ],
                             id="info-container",
                             className="row container-display",
                         ),
                     ],
                     id="right-column",
                     className="eight columns",
                 ),
             ],
             className="row flex-display",
         ),
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"},
)

# Main
if __name__ == "__main__":
    app.run_server(debug=True)
        
