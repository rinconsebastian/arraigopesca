from dash import html , dcc
import plotly.express as px

import dash_bootstrap_components as dbc

class linechart:
    def __init__(self, df, title, title_x, title_y, color, id):
        self.title = title
        self.title_x = title_x
        self.title_y = title_y
        self.color = color
        self.df = df
        self.id = id

    @staticmethod
    def figura(df,title_x,title_y,title):
        fig = px.line(df, x=title_x, y=title_y, title=title, height=350)
        # fig = px.line(df, x="year", y="lifeExp", title='Meses de mayor captura', height=350)
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