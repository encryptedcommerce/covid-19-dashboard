from typing import Dict, List, Optional

from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from models import header as model


@app.callback(
    Output('account-selector-dropdown', 'options'),
    [
        Input('date-picker-range', 'start_date'),
        Input('date-picker-range', 'end_date'),
        Input('url', 'pathname'),
    ]
)
def get_account_options(start_date: str, end_date: str, url: str = None) -> List[Dict[str, str]]:
    """Gets list of account IDs for use in Dropdown for account selection.

    Arguments:
        start_date: Start of date range to get data for.
        end_date: End of date range to get data for.
        url: URL of active pane, used to track changes and re-trigger callback.

    Returns:
        List of unique account IDs in table data.
    """
    account_options = model.get_account_codes(start_date, end_date)
    dropdown_options = [{'label': i, 'value': i} for i in account_options if i is not None]
    if not dropdown_options:
        dropdown_options = [{'label': 'No Data for Selected Date Range', 'value': ''}]
    return dropdown_options


@app.callback(
    Output('local', 'data'),
    [
        Input('account-selector-dropdown', 'options'),
        Input('account-selector-dropdown', 'value'),
    ],
    [State('local', 'data')]
)
def store_account_value(
        available_options: List[Dict[str, str]],
        selected_value: Optional[str] = None,
        data: Optional[Dict[str, str]] = None
):
    if available_options is None:
        # Prevent the None callbacks for the store component.
        raise PreventUpdate

    # Set a default value if there's no data.
    selected_value = selected_value or available_options[0].get('value')
    selected_value = selected_value or ''
    data = data or {'selected_value': selected_value}
    data['selected_value'] = selected_value

    return data


@app.callback(
    Output('account-selector-dropdown', 'value'),
    # Since we use the data prop in an output,
    # we cannot get the initial data on load with the data prop.
    # To counter this, you can use the modified_timestamp
    # as Input and the data as State.
    # This limitation is due to the initial None callbacks
    # https://github.com/plotly/dash-renderer/pull/81
    [
        Input('local', 'modified_timestamp'),
        Input('url', 'pathname'),
    ],
    [State('local', 'data')]
)
def set_account_value(
        ts,
        dummy_url : Optional[str] = None,
        data: Optional[str] = None
):
    """Set account drop-down value from local store, to persist selection between URL changes.

    Arguments:
        ts: Modification timestamp of local store.
        dummy_url: URL of active pane, used to track changes and re-trigger callback.
        data: Data object of local store.

    """
    if ts is None:
        raise PreventUpdate

    data = data or {}

    return data.get('selected_value', '')


