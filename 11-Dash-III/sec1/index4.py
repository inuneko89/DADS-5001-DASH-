import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
from app import app
from apps import scatter_layout, histogram_layout, line_layout, treemap_layout

# External stylesheets
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Create Dash app instance
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Sidebar style
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# Content style
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# Sidebar layout
sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P("A simple sidebar layout with navigation links", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Scatter", href='/apps/scatter_layout', active="exact"),
                dbc.NavLink("Line Chart", href='/apps/line_layout', active="exact"),  # เปลี่ยนเมนูที่สามเป็น Line Chart
                dbc.NavLink("Treemap", href='/apps/treemap_layout', active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

# Content layout
content = html.Div(id="page-content", style=CONTENT_STYLE)

# App layout
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# Callback to render page content based on URL pathname
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def render_page_content(pathname):
    if pathname == '/apps/scatter_layout':
        return scatter_layout.layout
    elif pathname == '/apps/line_layout':  # เพิ่มการตรวจสอบ URL สำหรับ Line Chart
        return line_layout.layout
    elif pathname == '/':
        return "Please choose a link"
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

if __name__ == "__main__":
    app.run_server(debug=False)
