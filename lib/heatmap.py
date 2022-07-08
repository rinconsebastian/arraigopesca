from dash import html , dcc
import plotly.express as px

import dash_bootstrap_components as dbc

class heatmap:
    def __init__(self, df, title, title_x, title_y, color, id):
        self.title = title
        self.title_x = title_x
        self.title_y = title_y
        self.color = color
        self.df = df
        self.id = id

    @staticmethod
    def figura(df,title_x,title_y,title):
        center_lat = df.lat.mean()-2
        center_lon = df.lon.mean()
        fig = px.density_mapbox(df, lat=title_x, lon=title_y, center={'lat':center_lat, 'lon':center_lon},zoom=5, mapbox_style='stamen-terrain', radius=10)
        fig.update_layout(title_text=title, height=750)
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