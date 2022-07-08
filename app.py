# Basics Requirements
from dash import Dash, dcc,  html, callback, Input, Output
import dash_bootstrap_components as dbc
from lib.heatmap import heatmap
from lib.linechart import linechart
from dash.dependencies import State
from lib.predictor import predictor


# Dash instance declaration
request_path_prefix = None
app = Dash(__name__, requests_pathname_prefix=request_path_prefix, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}], suppress_callback_exceptions=True)
app.title = 'Dashboard team 25 - cohort 6 Colombia Correlation One'  

# LOAD THE DIFFERENT FILES
from pages import dashboard, acercade, evaluacion
from lib import title

from lib.barchart import barchart
from data.process import especies, ingresos, mapData, artes, months
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
        return html.Div([evaluacion.evaluacion])
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
    Input('cuenca_dropdown', 'value'),
    Input('age-slider', 'value')
)
def update_outputmap(valuecuenca,valueedad):
    df1 = mapData(valuecuenca,valueedad)
    fig1 = heatmap(df1,"Heatmap","lat","lon","","bc1")
    return fig1.display()


#############################################################
# Fig 2 Species
#############################################################
@app.callback(
    Output('idfig1', 'children'),
    Input('cuenca_dropdown', 'value'),
    Input('age-slider', 'value')
)
def update_output(valuecuenca,valueedad):
    df2 = especies(valuecuenca,valueedad)
    fig2 = barchart(df2,"Especies","Especie","Valor","","bc2s")
    return fig2.display()


#############################################################
# Fig 3 Arts
#############################################################
@app.callback(
    Output('idfig3', 'children'),
    Input('cuenca_dropdown', 'value'),
    Input('age-slider', 'value')
)
def update_output3(valuecuenca,valueedad):
    df3 = artes(valuecuenca,valueedad)
    fig3 = barchart(df3,"Artes de pesca","artes_metodos","artes_conteo","","bc3s")
    return fig3.display()


#############################################################
# Fig 4 Months
#############################################################
@app.callback(
    Output('idfig4', 'children'),
    Input('cuenca_dropdown', 'value'),
    Input('age-slider', 'value')
)
def update_output4(valuecuenca,valueedad):
    df4 = months(valuecuenca,valueedad)
    fig4 = linechart(df4,"Meses de mayor captura","Mes","Valor","","bc4s")
    return fig4.display()

#############################################################
# Fig 5 Ingresos
#############################################################
@app.callback(
    Output('idfig5', 'children'),
    Input('cuenca_dropdown', 'value'),
    Input('age-slider', 'value')
)
def update_output5(valuecuenca,valueedad):
    df5 = ingresos(valuecuenca,valueedad)
    fig5 = barchart(df5,"Ingreso provenientes de la activdad pesquera","Rango","Porcentaje","","bc5s")
    return fig5.display()


'''
@app.callback(
    Output('edad', 'children'),
    [Input('age-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

'''

#############################################################
# Form 
#############################################################
@app.callback(
    Output('outPrediccion', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('edad-row', 'value'),
     State('ingresos-row', 'value'),
     State('faenas-row', 'value'),
     State('kg-row', 'value'),
     State('artes-checklist-input', 'value'),
     State('especies-checklist-input', 'value'),
     State('meses-checklist-input', 'value'),
     State('precio-row', 'value'),
     State('ingresoprom-row', 'value'),
     State('gastoprom-row', 'value'),
     State('cuenca-row', 'value'),
     ])
def compute(n_clicks, input1, input2, input3, input4, input5, input6, input7, input8, input9, input10, input11):
    
    if((input1) and (input2) and (input3) and (input4) and (input5)and (input6) and (input7)and (input8) and (input9 != 1) and (input10 != 1) and (input11 != 1)):
        return predictor([input1, input2, input3, input4, input5, input6, input7, input8, input9, input10, input11])
    else:
        return dbc.Alert("Diligencie el formulario completo", color="danger"),
   
    

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
