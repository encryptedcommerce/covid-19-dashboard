from typing import Dict, List

from dash.dependencies import Input, Output, State

from app import app
from controllers import common
from models import deaths as model
from views import deaths as view
from views.translations import localize


# Controller module-level cache from model data
CACHE = {
    'table_data': None,
    'table_csv': None,
    'table_rows': None,
    'chart_data': None,
}


def get_data(cache_key: str):
    """Get data from cache or underlying model."""
    global CACHE

    if cache_key not in CACHE:
        print('** Error: attempt to retrieve data with invalid cache key.')
        return
    if CACHE[cache_key] is None:
        if cache_key == 'table_data':
            CACHE[cache_key] = model.get_table_data()
        elif cache_key == 'table_csv':
            CACHE[cache_key] = common.get_table_csv(model)
        elif cache_key == 'table_rows':
            CACHE[cache_key] = common.get_table_rows(model)
        elif cache_key == 'chart_data':
            CACHE[cache_key] = model.get_chart_data()

    return CACHE[cache_key]


@app.callback(Output('tab-heading-deaths', 'children'), [Input('url', 'pathname')])
def localize_heading(dummy_url: str = None) -> str:
    return localize('deaths')


@app.callback(Output('tabs-content-deaths', 'children'),
              [Input('tabs-deaths', 'value')])
def render_tab_content(tab):
    return common.render_tab_content(view, tab)


@app.callback(
    Output('deaths-table-component', 'columns'),
    [
        Input('url', 'pathname'),
    ]
)
def get_table_columns(dummy_url: str = None) -> List[dict]:
    """Get column headers for DataTable.

    Arguments:
        dummy_url: URL of active pane, used to track URL changes and re-trigger callback.

    Returns:
        List of header objects.

    """
    data = get_data('table_data')
    table_columns = [{"name": i.title(), "id": i} for i in data.columns]

    return table_columns


@app.callback(
    Output('deaths-table-component', 'data'),
    [
        Input('url', 'pathname'),
    ]
)
def get_table_rows(dummy_url: str = None) -> List[dict]:
    """Get Scoring Time table rows, for use by DataTable.

    Arguments:
        dummy_url: URL of active pane, used to track URL changes and re-trigger callback.

    Returns:
        List of table rows.
    """
    rows = get_data('table_rows')
    return rows


@app.callback(
    Output('deaths-download-link', 'href'),
    [
        Input('url', 'pathname'),
    ]
)
def get_table_csv(dummy_url: str = None):
    """Gets Scoring Time table data in CSV format, for downloading purposes.

    Arguments:
        dummy_url: URL of active pane, used to track changes and re-trigger callback.

    Returns:
        CSV data with UTF-8 encoding for use as data: element in download href.
    """
    csv = get_data('table_csv')
    return csv


@app.callback(
    Output('deaths-chart-component', 'figure'),
    [
        Input('deaths-country-selector-dropdown', 'value'),
        Input('url', 'pathname'),
    ]
)
def get_chart_figure(selected_countries = None, dummy_url: str = None):
    """Gets Scoring Time figure for use by graph object.

    Arguments:
        selected_countries: Countries to include in the chart.
        dummy_url: URL of active pane, used to track changes and re-trigger callback.

    Returns:
        Object with chart data and layout.
    """
    chart_data = get_data('chart_data')

    # Filter data by selected countries.
    if selected_countries is None or not selected_countries:
        chart_data = [series for series in chart_data]
    else:
        chart_data = [series for series in chart_data if series.get('name') in selected_countries]

    figure = {
        'data': chart_data,
        'layout': {
            'title': localize('deaths'),
            'hovermode': 'closest',
        },
    }
    return figure


@app.callback(
    Output('deaths-country-selector-dropdown', 'options'),
    [
        Input('url', 'pathname'),
    ]
)
def get_country_options(dummy_url: str = None) -> List[Dict[str, str]]:
    """Get list of country IDs for use in Dropdown for chart country selection.

    Arguments:
        dummy_url: URL of active pane, used to track changes and re-trigger callback.

    Returns:
        List of unique country names in table data.
    """
    return common.get_country_options(model)


@app.callback(
    Output('deaths-country-selector-dropdown', 'value'),
    [
        Input('deaths-country-selector-dropdown', 'options'),
    ]
)
def set_country_value(available_options) -> List[str]:
    """Set default values for Deaths countries selector."""
    if available_options is None:
        return ['No Data is Available']
    else:
        values = [
            c.get('value') for c in available_options
        ]

        user_country = model.get_user_country()

        if user_country in values:
            index = values.index(user_country)
            return values[0:6] + [values[index]]
        else:
            return values[0:8]

