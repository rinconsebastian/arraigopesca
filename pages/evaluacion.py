# Basics Requirements
from dash import dcc,html
import dash_bootstrap_components as dbc

from lib.form import form

# Dash Bootstrap Components



evaluacion = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div(
            [form], className="widget widget2"
        )),
        dbc.Col(html.Div(
            [
             html.Div(
                   [],id="outPrediccion", className="col-texto-acerca" 
                ),
            ], className="widget")),
         
        ]  
    ),
])