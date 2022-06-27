from dash import html , dcc
import plotly.graph_objects as go

import dash_bootstrap_components as dbc

class bargroupedchart:
    def __init__(self, df, title, title_x, title_y, color, id):
        self.title = title
        self.title_x = title_x
        self.title_y = title_y
        self.color = color
        self.df = df
        self.id = id

    @staticmethod
    def figura(df,title_x,title_y,title):
        fig = go.Figure(data=df)
        # Change the bar mode
        fig.update_layout(barmode='group')
        fig.update_layout(title_text=title, height=350)
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