import os

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import send_from_directory

from app import app
import views
# Necessary for all controllers' callbacks to apply:
import controllers  # noqa  # pylint: disable=unused-import

app.title = 'COVID-19 Dashboard'

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    views.header,
    html.Div(id='left-nav'),
    html.Div(id='pane-content'),
])


@app.callback(Output('left-nav', 'children'), [Input('url', 'pathname')])
def highlight_navbar(pathname):
    return views.navbar.create_navbar(pathname)


@app.callback(Output('pane-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    routes = {
        '/': views.summary_dashboard.layout,
        '/confirmed': views.confirmed.layout,
        '/deaths': views.deaths.layout,
        '/recovered': views.recovered.layout,
    }
    if pathname in routes:
        return routes[pathname]
    else:
        return 'The resource you have requested is not found.'


@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)

server = app.server

if __name__ == '__main__':
    env = os.environ.get('ENV', 'PROD')
    if env.upper() in ['LOCAL']:
        debug_toolbar = True
    else:
        debug_toolbar = False
    app.run_server(host='0.0.0.0', debug=debug_toolbar)
