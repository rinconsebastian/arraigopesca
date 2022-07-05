# Basics Requirements
from dash import dcc


# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Recall app
from app_ds4f import app

############################################################################
#
# ELEMENTS
#
#############################################################################

#############################################################################
# Basin Dropdown
#############################################################################

dropdown = dcc.Dropdown(
    id="cuenca_dropdown",
    options=[{"label":"Cauca" , "value":"RÍO CAUCA" },
    {"label":"Magdalena" , "value":"RÍO MAGDALENA" },
    {"label":"San Jorge" , "value":"RÍO SAN JORGE" },
    {"label":"Sinú" , "value":"RÍO SINÚ" },],
    value=["RÍO CAUCA", "RÍO MAGDALENA","RÍO SAN JORGE","RÍO SINÚ"],
    multi=True,
)
#############################################################################
# Basin Dropdown
#############################################################################

age_slider = dcc.RangeSlider(15, 100, step=10, value=[0, 120], id='age-slider')

############################################################################
#
# LAYOUT
#
#############################################################################

filters = dbc.Row([
    dbc.Col(dropdown),
    dbc.Col(age_slider),
    dbc.Col()
    ],
    className="filters"  
)

