# Basics Requirements
from dash import Dash, dcc,  html, callback, Input, Output
import dash_bootstrap_components as dbc
from lib.heatmap import heatmap



# Dash instance declaration
request_path_prefix = None
app = Dash(__name__, requests_pathname_prefix=request_path_prefix, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}], suppress_callback_exceptions=True)
app.title = 'Dashboard team 25 - cohort 6 Colombia Correlation One'  

# LOAD THE DIFFERENT FILES
from pages import dashboard, acercade
from lib import title

from lib.barchart import barchart
from data.process import especies, mapData

###########################################################
#
#           APP LAYOUT:
#
###########################################################
server = app.server


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
# Fig 1 Heatmap
#############################################################
@app.callback(
    Output('idmap', 'children'),
    Input('cuenca_dropdown', 'value')
)
def update_outputmap(value):
    df1 = mapData(value)
    fig1 = heatmap(df1,"Heatmap","lat","lon","","bc1")
    return fig1.display()


#############################################################
# Fig 2 Species
#############################################################
@app.callback(
    Output('idfig1', 'children'),
    Input('cuenca_dropdown', 'value')
)
def update_output(value):
    df2 = especies(value)
    fig2 = barchart(df2,"Especies","Especie","Valor","","bc2s")
    return fig2.display()


#############################################################
# TREEMAP PLOT : Add sidebar interaction here
#############################################################


#############################################################
# MAP : Add interactions here
#############################################################

# MAP date interaction


# MAP click interaction


if __name__ == "__main__":
    app.run_server(debug=True)
