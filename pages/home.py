# Home page skeleton
#
# AUTHOR Sven Schrodt
# SINCE 2026-01-16

from dash import (
    Dash,
    html,
    dash_table,
    dcc,
    callback,
    Output,
    Input,
    State,
    register_page,
)
from pmonlib.dd import DD

register_page(__name__, path="/")


layout = html.Div(
    [
        html.Div([html.H1("Dash app skeleton"), html.P("Foo"),  html.Img(src="assets/favicon.svg")])
    ]
)
