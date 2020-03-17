from dash.dependencies import Input, Output

from app import app
from views.translations import localize


@app.callback(Output('summary-welcome', 'children'), [Input('url', 'pathname')])
def localize_summary_welcome(dummy_url: str = None) -> str:
    return localize('summary-welcome')


@app.callback(Output('summary-intro', 'children'), [Input('url', 'pathname')])
def localize_summary_intro(dummy_url: str = None) -> str:
    return localize('summary-intro')


@app.callback(Output('summary-description', 'children'), [Input('url', 'pathname')])
def localize_summary_description(dummy_url: str = None) -> str:
    return localize('summary-description')


@app.callback(Output('data-credit', 'children'), [Input('url', 'pathname')])
def localize_data_credit(dummy_url: str = None) -> str:
    return localize('data-credit')


@app.callback(Output('data-update', 'children'), [Input('url', 'pathname')])
def localize_data_update(dummy_url: str = None) -> str:
    return localize('data-update')


@app.callback(Output('geoip-credit', 'children'), [Input('url', 'pathname')])
def localize_geoip_credit(dummy_url: str = None) -> str:
    return localize('geoip-credit')
