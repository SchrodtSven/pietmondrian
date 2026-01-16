# Admin page skeleton
#
# AUTHOR Sven Schrodt
# SINCE 2026-01-16

from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from pmonlib.dd import DD

register_page(__name__)

# Daten laden
layout = html.Div(
    [
        # Hero Section
        html.Div(
            [html.H1("Admin page"), html.P("Lorem Ipsum Foo")],
        )
    ]
)
