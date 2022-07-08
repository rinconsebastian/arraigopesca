# Basics Requirements
from dash import dcc,html


# Dash Bootstrap Components
import dash_bootstrap_components as dbc


#Components
from lib import filters 

#Data
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

import numpy as np

from app_ds4f import app

from lib.piechart import piechart
from lib.linechart import linechart
from lib.bargroupedchart import bargroupedchart
from lib.heatmapchart import heatmapchart
from lib.distmultiplechart import distmultiplechart
from lib.heatmap import heatmap
from lib.predictor import predictor


############################################################################
#
# ELEMENTS
#
#############################################################################




#############################################################################
# Fig 2
#############################################################################

# This dataframe has 244 lines, but 4 distinct values for `day`
df2 = px.data.tips()
fig2 = piechart(df2,"Pertenence a una organización pesquera","tip","day","","bc2") 
# px.pie(df2, values='tip', names='day', title='Pertenence a una organización pesquera', height=350)


#############################################################################
# Fig 3
#############################################################################

df3 = px.data.gapminder().query("country=='Canada'")
fig3 = linechart(df3,"Pertenence a una organización pesquera","year","lifeExp","","bc3") 
# fig3 = px.line(df3, x="year", y="lifeExp", title='Meses de mayor captura', height=350)


#############################################################################
# Fig 4
#############################################################################

animals=['giraffes', 'orangutans', 'monkeys']
df4 = [
    go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
    go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
]
fig4 = bargroupedchart(df4,'Costos totales de pesca',"","","","bc4") 


#############################################################################
# Fig 5
#############################################################################
df5 = go.Heatmap(
                    z=[[1, 20, 30],
                      [20, 1, 60],
                      [30, 60, 1]],
                    text=[['one', 'twenty', 'thirty'],
                          ['twenty', 'one', 'sixty'],
                          ['thirty', 'sixty', 'one']],
                    texttemplate="%{text}",
                    textfont={"size":20})
fig5 = heatmapchart(df5,'Porcentaje de ingresos por pesca',"","","","bc5") 

#############################################################################
# Fig 6
#############################################################################
x1 = np.random.randn(200) - 1
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 1

df6 = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']
colors = ['#835AF1', '#7FA6EE', '#B8F7D4']
fig6 = distmultiplechart(df6,'Distribución del precio promedio de venta',group_labels,"",colors,"bc6") 

#############################################################################
# Predictor
#############################################################################

valores = [['0.9373207470646803', '0.5578861300061824', '0.6775102514642114',
        '-0.17361004280264897', '0.0', '1.0', '0.0', '0.0', '0.0', '0.0',
        '0.0', '0.0', '0.0', '1.0', '0.0', '0.0', '0.0', '0.0', '1.0',
        '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '1.0', '0.0', '0.0',
        '0.0', '0.0', '0.0', '1.0', '0.0', '0.0', '0.0', '0.0', '0.0',
        '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '6000.0',
        'Menos de $ 500.000', 'Menos de $ 500.000', 'RÍO MAGDALENA']]



############################################################################
#
# LAYOUT
#
#############################################################################

dashboard = dbc.Container([
    dbc.Row([filters.filters]),
    dbc.Row([
        dbc.Col([html.Img(src=app.get_asset_url("loading.gif"), height="300px", className="mr-10")], sm=12, md=6, id="idmap" , class_name="height100"),
        dbc.Col([
            dbc.Row([
                dbc.Col([html.Img(src=app.get_asset_url("loading.gif"), height="300px", className="mr-10")], sm=12, md=6, id="idfig1"),
                dbc.Col([html.Img(src=app.get_asset_url("loading.gif"), height="300px", className="mr-10")], sm=12, md=6, id="idfig3"),
            ]),
            dbc.Row([
                dbc.Col([html.Img(src=app.get_asset_url("loading.gif"), height="300px", className="mr-10")], sm=12, md=6, id="idfig4"),
                dbc.Col([html.Img(src=app.get_asset_url("loading.gif"), height="300px", className="mr-10")], sm=12, md=6, id="idfig5"),
            ]),
    
        ], sm=12, md=6),
       

    ], class_name="heighHv"),
  
   
]
,className="dashboard"  
)

