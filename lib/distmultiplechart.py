from dash import html , dcc
import plotly.figure_factory as ff

import dash_bootstrap_components as dbc

class distmultiplechart:
    def __init__(self, df, title, title_x, title_y, color, id):
        self.title = title
        self.title_x = title_x
        self.title_y = title_y
        self.color = color
        self.df = df
        self.id = id

    @staticmethod
    def figura(df,title_x,title_y,title,color):

        # Create distplot with curve_type set to 'normal'
        fig = ff.create_distplot(df, title_x, colors=color, bin_size=.25, show_curve=False)
        fig.update_layout(title_text=title, height=350)
        return fig
        



    def display(self):
        layout = html.Div(
            [
             html.Div([
                    dcc.Graph(figure=self.figura(self.df,self.title_x,self.title_y,self.title,self.color))
                ]),
            ],id=self.id, className="widget"
        )
        return layout