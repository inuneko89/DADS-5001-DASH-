from dash import Dash
import dash_bootstrap_components as dbc

app = Dash(__name__)
server = app.server
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])