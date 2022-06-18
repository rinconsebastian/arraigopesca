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
    id="basin_dropdown",
    options=[{"label":"Cauca" , "value":"cauca" },
    {"label":"Magdalena" , "value":"magdalena" },
    {"label":"San Jorge" , "value":"san_jorge" },
    {"label":"Sinú" , "value":"sinu" },],
    value=["cauca", "magdalena","san_jorge","sinu"],
    multi=True,
)
############################################################################
#
# LAYOUT
#
#############################################################################

filters = dbc.Row([
    dbc.Col(dropdown),
    dbc.Col(),
    dbc.Col()
    ],
    className="filters"  
)

