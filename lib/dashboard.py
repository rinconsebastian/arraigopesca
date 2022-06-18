# Basics Requirements
from dash import dcc


# Dash Bootstrap Components
import dash_bootstrap_components as dbc


#Components
from lib import filters 

#Data
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

import numpy as np
############################################################################
#
# ELEMENTS
#
#############################################################################
#############################################################################
# Fig 1
#############################################################################

df1 = px.data.gapminder().query("country == 'Canada'")
fig1 = px.bar(df1, x='year', y='pop', height=350)
fig1.update_layout(title_text='Especie capturada')


#############################################################################
# Fig 2
#############################################################################

# This dataframe has 244 lines, but 4 distinct values for `day`
df2 = px.data.tips()
fig2 = px.pie(df2, values='tip', names='day', title='Pertenence a una organización pesquera', height=350)


#############################################################################
# Fig 3
#############################################################################

df3 = px.data.gapminder().query("country=='Canada'")
fig3 = px.line(df3, x="year", y="lifeExp", title='Meses de mayor captura', height=350)


#############################################################################
# Fig 4
#############################################################################

animals=['giraffes', 'orangutans', 'monkeys']

fig4 = go.Figure(data=[
    go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
    go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
])
# Change the bar mode
fig4.update_layout(barmode='group')
fig4.update_layout(title_text='Costos totales de pesca', height=350)

#############################################################################
# Fig 5
#############################################################################

fig5 = go.Figure(data=go.Heatmap(
                    z=[[1, 20, 30],
                      [20, 1, 60],
                      [30, 60, 1]],
                    text=[['one', 'twenty', 'thirty'],
                          ['twenty', 'one', 'sixty'],
                          ['thirty', 'sixty', 'one']],
                    texttemplate="%{text}",
                    textfont={"size":20}))

fig5.update_layout(title_text='Porcentaje de ingrwesos por pesca', height=350)
#############################################################################
# Fig 6
#############################################################################



x1 = np.random.randn(200) - 1
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 1

hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']
colors = ['#835AF1', '#7FA6EE', '#B8F7D4']

# Create distplot with curve_type set to 'normal'
fig6 = ff.create_distplot(hist_data, group_labels, colors=colors, bin_size=.25,
                         show_curve=False)

# Add title
fig6.update_layout(title_text='Distribución del precio promedio de venta', height=350)




############################################################################
#
# LAYOUT
#
#############################################################################

dashboard = dbc.Container([
    dbc.Row([filters.filters]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig1, id="barPlot1")),
        dbc.Col(dcc.Graph(figure=fig2, id="piePlot")),
        dbc.Col(dcc.Graph(figure=fig3, id="linePlot")),

    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig4, id="barPlot2")),
        dbc.Col(dcc.Graph(figure=fig5, id="heatmapPlot")),
        dbc.Col(dcc.Graph(figure=fig6, id="distributionPlot")),

    ]),
]
,className="dashboard"  
)

