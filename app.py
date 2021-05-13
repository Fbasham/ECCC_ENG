import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
from dataframes import *

# default stationID
DEFAULT = '04LG004'

# setup and use user defined styles
external_stylesheets = [
    './assets/styles.css',
    {
    'href': 'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
    'rel': 'stylesheet',
    'integrity': 'sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf',
    'crossorigin': 'anonymous'
    }
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# this is needed for the Heroku deployment
server = app.server

# instantiate the layout using semantic HTML components provided by dash
app.layout = html.Div(children=[
    html.Div(id='head',children=[
        html.H2(children='Water Quantity Data'),
        html.Div(children=[
            html.Div(children=[
                html.I(className="fas fa-user"),
                html.Span(' Frank Basham')
            ]),
            html.Div(children=[
                html.I(className="fab fa-github"),
                html.A(' GitHub',href='https://github.com/Fbasham/ECCC_ENG',target='_blank'),
            ])
        ])
    ]),

    html.H3(id='stationName',children=f"STATION: {df_stations.at[DEFAULT,'StationName']}"),

    html.Div([
                dcc.Dropdown(
                    id='stationID',
                    options=[{'label': i, 'value': i} for i in df_stations.index],
                    value=DEFAULT
                )
            ]
    ),
    
    dcc.Graph(id='flow-graphic'),

    dcc.Graph(id='level-graphic'),
])


# callbacks that define the logic upon changing the dropdown item (stationID)

@app.callback(
    Output('flow-graphic', 'figure'),
    Output('stationName', 'children'),
    Input('stationID', 'value'))
def update_graph(station_ID=DEFAULT):
    df = df_flows[df_flows['ID'] == station_ID]
    station = df_stations.at[station_ID,'StationName']
    dfh = df_historical_flows[df_historical_flows['ID'] == station_ID]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=dfh['Date'], 
            y=dfh['Flow(m³/s)'],
            name='historical'
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df['Date'], 
            y=df['Flow (m3/s)'],
            name='realtime'
        )
    )
    fig.update_xaxes(title_text='Date')
    fig.update_yaxes(title_text='Flow (m³/s)')
    fig.update_layout(title='Discharge')
    return fig, f"STATION: {station}"


@app.callback(
    Output('level-graphic', 'figure'),
    Input('stationID', 'value'))
def update_graph(station_ID=DEFAULT):
    df = df_levels[df_levels['ID'] == station_ID]
    dfh = df_historical_levels[df_historical_levels['ID'] == station_ID]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=dfh['Date'], 
            y=dfh['Level(m)'],
            name='historical',
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df['Date'], 
            y=df['Level (m)'],
            name='realtime'
        )
    )
    fig.update_xaxes(title_text='Date')
    fig.update_yaxes(title_text='Level (m)')
    fig.update_layout(title='Stage')
    return fig


# run the server 
if __name__ == '__main__':
    app.run_server(debug=True)