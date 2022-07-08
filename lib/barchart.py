from dash import html , dcc
import plotly.express as px

import dash_bootstrap_components as dbc

class barchart:
    def __init__(self, df, title, title_x, title_y, color, id):
        self.title = title
        self.title_x = title_x
        self.title_y = title_y
        self.color = color
        self.df = df
        self.id = id

    @staticmethod
    def figura(df,title_x,title_y,title):
        fig = px.bar(df, x=title_x, y=title_y, height=350) #  'year', y='pop'
        fig.update_layout(title_text=title, height=350, yaxis={"tickformat": ',.0%',"range": [0,1]})

        return fig
        



    def display(self):
        layout = html.Div(
            [
             html.Div([
                    dcc.Graph(figure=self.figura(self.df,self.title_x,self.title_y,self.title))
                ]),
            ],id=self.id, className="widget"
        )
        return layout