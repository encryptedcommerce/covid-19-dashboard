from dash.dependencies import Input, Output

from app import app
from views.translations import localize


@app.callback(Output('summary-dashboard', 'children'), [Input('url', 'pathname')])
def localize_summary_welcome(dummy_url: str = None) -> str:
    return localize('summary-dashboard')


@app.callback(Output('confirmed', 'children'), [Input('url', 'pathname')])
def localize_summary_intro(dummy_url: str = None) -> str:
    return localize('confirmed')


@app.callback(Output('deaths', 'children'), [Input('url', 'pathname')])
def localize_summary_description(dummy_url: str = None) -> str:
    return localize('deaths')


@app.callback(Output('recovered', 'children'), [Input('url', 'pathname')])
def localize_summary_description(dummy_url: str = None) -> str:
    return localize('recovered')


@app.callback(Output('chart-tab', 'label'), [Input('url', 'pathname')])
def localize_summary_description(dummy_url: str = None) -> str:
    return localize('chart')


@app.callback(Output('table-tab', 'label'), [Input('url', 'pathname')])
def localize_summary_description(dummy_url: str = None) -> str:
    return localize('table')

