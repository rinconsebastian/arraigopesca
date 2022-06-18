# Basics Requirements
from dash import dcc,  html, callback, Input, Output


# Dash Bootstrap Components
import dash_bootstrap_components as dbc


# Data


# Recall app
from app_ds4f import app

###########################################################
#
#           APP LAYOUT:
#
###########################################################

# LOAD THE DIFFERENT FILES
from lib import title,dashboard, acercade


# PLACE THE COMPONENTS IN THE LAYOUT
app.layout = dbc.Container(
    [  # represents the browser address bar and doesn't render anything
        dcc.Location(id='url', refresh=False),

        dbc.Row([
            dbc.Col([title.title], width= 12),
        ]),
        dbc.Row([
              ## dbc.Col([sidebar.sidebar], width= 3, md=4, lg=3, xl=2, xxl=1 ),
              dbc.Col("", width= 12, id="content"),
        ], className=["fullHeight","max-width-50"]),
        ],
    className="container-t25",  # You can also add your own css files by storing them in the assets folder
)

###############################################
#
#           APP INTERACTIVITY:
#
###############################################

###############################################################
# Load the three pages
#################################################################
@callback(Output('content', 'children'),[Input('url', 'pathname')])
def display_page(pathname):
    
    if pathname == "/":
        return html.Div([dashboard.dashboard])
    elif pathname == "/evaluacion":
        return "arraigo"
    elif pathname == "/acercade":
        return html.Div([acercade.acercade])
    else:
        return "Pagina no existe"

#############################################################
# Nav bar buttons color
#############################################################
@app.callback(Output('btn-dashboard', 'className'), [Input('url', 'pathname')])
def change_button_style(pathname):
    if pathname == "/" :
        return "nav-item-active"
    else:
        return  ""

@app.callback(Output('btn-evaluacion', 'className'), [Input('url', 'pathname')])
def change_button_style(pathname):
    if pathname == "/evaluacion" :
        return "nav-item-active"
    else:
        return  ""

@app.callback(Output('btn-acercade', 'className'), [Input('url', 'pathname')])
def change_button_style(pathname):
    if pathname == "/acercade" :
        return "nav-item-active"
    else:
        return  ""
       

#############################################################
# PROFITS BY CATEGORY : Add sidebar interaction here
#############################################################


#############################################################
# TREEMAP PLOT : Add sidebar interaction here
#############################################################


#############################################################
# MAP : Add interactions here
#############################################################

# MAP date interaction


# MAP click interaction


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8050", debug=True)
