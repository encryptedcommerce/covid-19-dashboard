import urllib.parse
from typing import Dict, List


def get_table_rows(model) -> List[dict]:
    """Get list of rows for DataTable, for use across all panes.

    Arguments:
        model: The model module to use for data retrieval.

    Returns:
        Table rows for DataTable.
    """
    table_data = model.get_table_data()
    table_rows = table_data.to_dict('rows')
    return table_rows


def get_table_csv(
        model,
        dummy_url: str = None
):
    """Get table data in CSV format for downloading purposes, for use across all panes.

    Arguments:
        model: The model module to use for data retrieval.
        dummy_url: URL of active pane, used to track changes and re-trigger callback.

    Returns:
        CSV data with UTF-8 encoding for use as data: element in download href.
    """
    table_data = model.get_table_data()
    csv_string = table_data.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
    return csv_string


def get_country_options(model) -> List[Dict[str, str]]:
    """Get list of country IDs for use in country selection dropdowns, for use across all panes.

    Arguments:
        model: The model module to use for data retrieval.

    Returns:
        List of unique country IDs in table data.
    """
    table_data = model.get_table_data()
    country_options = list(table_data['Country/Region'].unique())
    dropdown_options = [{'label': i, 'value': i} for i in country_options]
    return dropdown_options


def render_tab_content(view, tab):
    if tab == 'tab-1-chart':
        return view.get_chart_layout()
    elif tab == 'tab-2-table':
        return view.get_table_layout()

