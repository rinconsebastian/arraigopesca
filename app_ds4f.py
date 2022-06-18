#######################################################
# Main APP definition.
#
# Dash Bootstrap Components used for main theme and better
# organization.
#######################################################

from dash import Dash
import dash_bootstrap_components as dbc




request_path_prefix = None


app = Dash(__name__, requests_pathname_prefix=request_path_prefix, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])
app.title = 'Dashboard team 25 - cohort 6 Colombia Correlation One'  

#server = app.server

# We need this for function callbacks not present in the app.layout
app.config.suppress_callback_exceptions = True
