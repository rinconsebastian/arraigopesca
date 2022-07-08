# Basics Requirements
from dash import html


# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Recall app
from app_ds4f import app


acercade = dbc.Container(
    [dbc.Row([
        dbc.Col([
            html.P("Este proyecto es realizado por estudiantes en el marco del programa Data Science For All del Ministerio de las Tecnologías e Información de las Comunicaciones (MINTIC) en alianza con Correlation One."),
            html.P("Agradecemos a la AUNAP (Autoridad Nacional de Acuicultura y Pesca) y PNUD (Programa de las Naciones Unidas para el Desarrollo) por brindarnos acceso a los datos, y entendemos la importancia de esta información como  insumo para la definición de políticas públicas, programas y proyectos que fortalezcan la actividad pesquera a través de condiciones dignas para quienes la practican, sensibilizando sobre su importancia para la seguridad alimentaria del país y contribuyendo al Objetivo de Desarrollo Sostenible 14”, Conservar y utilizar de forma sostenible los océanos, los mares y los recursos marinos para el desarrollo sostenible."),
    ], width= 12,  md=8,className="col-texto-acerca"),
        dbc.Col(
            html.Img(src=app.get_asset_url("Imagenpescador.png"),  className="pescador-acerca")
            , width= 12,  md=4, className="")
    ] ,className="row1-acerca"),
    dbc.Row([
        dbc.Col(html.Img(src=app.get_asset_url("ImgMinTIC.png"),  className=""),  className="col-logo-acerca"),
        dbc.Col(html.Img(src=app.get_asset_url("ImgC1.png"),  className=""),  className="col-logo-acerca"),
        dbc.Col(html.Img(src=app.get_asset_url("ImgAUNAP.png"),  className=""),  className="col-logo-acerca"),
        dbc.Col(html.Img(src=app.get_asset_url("ImgPNUD.png"),  className=""),  className="col-logo-acerca"),



    ])



    ]


)