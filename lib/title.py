# Basics Requirements

from dash import  Input, Output, State,html

# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Recall app
from app_ds4f import app

menus = dbc.Row(
    [
        dbc.NavItem(dbc.NavLink("DASHBOARD", href="/"), className="nav-item-active", id="btn-dashboard"),
        dbc.NavItem(dbc.NavLink("EVALUACIÓN DE ARRAIGO", href="/evaluacion"), id="btn-evaluacion"),
        dbc.NavItem(dbc.NavLink("ACERCA DE", href="/acercade"), id="btn-acercade"),
    ],
    className="g-0 ms-auto mt-3 mt-md-0",
    align="right",
)



title = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=app.get_asset_url("aunap_white.svg"), height="50px", className="mr-10")),
                        dbc.Col(dbc.NavbarBrand(["DASHBOARD ARRAIGO", html.Br()," PESCA ARTESANAL"], className="ml-10")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="#",
                style={"textDecoration": "none"},
            ),
            
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                menus,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="#3065c7",
    dark=True,
    id="nav-bar"
)


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
