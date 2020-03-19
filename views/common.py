import json
from typing import Dict, List, Optional

import dash_core_components as dcc
import dash_html_components as html
import dash_table

from views.translations import localize


def get_scale_toggle(pane_id: str) -> html.Div:
    """Get y-axis scale toggle.

    Arguments:
        pane_id: DOM ID of pane.

    Returns:
        HTML component with scale toggle.
    """
    scale_options = [
        {'label': localize('log-scale'), 'value': 'log'},
        {'label': localize('linear-scale'), 'value': 'linear'}
    ]

    return html.Div(
        id=f'{pane_id}-scale-toggle',
        className='scale-toggle',
        children=[
            html.Span(
                localize('y-axis') + ': ',
                id=f'scale-toggle-label',
                className='scale-toggle-label'
            ),
            dcc.RadioItems(
                id=f'scale-toggle-options',
                className='scale-toggle-options',
                options=scale_options,
                value='log'
            )
        ]
    )


def get_tabs_layout(pane_id: str) -> html.Div:
    """Get standard layout with common components.

    Arguments:
        pane_id: DOM ID of pane.

    Returns:
        HTML component containing common subcomponents.
    """
    components = [
        html.H2(pane_id.replace('-', ' ').title(), id=f'tab-heading-{pane_id}')
    ]

    components.extend([
        dcc.Tabs(id=f'tabs-{pane_id}', value='tab-1-chart', children=[
            dcc.Tab(id='chart-tab', label='Chart', value='tab-1-chart'),
            dcc.Tab(id='table-tab', label='Table', value='tab-2-table'),
        ]),
        html.Div(id=f'tabs-content-{pane_id}')
    ])

    layout = html.Div(
        children=components
    )

    return layout


def get_table(
        pane_id: str,
        table_columns: List[Dict[str, str]],
        table_rows: List[dict],
        style_cell : Optional[dict] = None,
        style_cell_conditional: Optional[List[Dict[str, Dict[str, str]]]] = None
) -> html.Div:
    """Get DataTable for pane data.

    Arguments:
        pane_id: DOM ID of pane.
        table_columns: list of column objects.
        table_rows: list of rows.
        style_cell: object with default cell style.
        style_cell_conditional: object with conditional cell styles.

    Returns:
        HTML component with DataTable.
    """
    if style_cell is None:
        style_cell = {
            'width': '160px',
        }

    if style_cell_conditional is None:
        style_cell_conditional = []

    return html.Div(
        id=f'{pane_id}-table',
        children=[
            dash_table.DataTable(
                id=f'{pane_id}-table-component',
                columns=table_columns,
                data=table_rows,
                filter_action='native',
                fixed_rows={'headers': True, 'data': 0},
                sort_action='native',
                style_table={
                    'width': '100%',
                    'maxHeight': '300',
                    'overflowY': 'scroll'
                },
                style_cell=style_cell,
                style_cell_conditional=style_cell_conditional
            )
        ]
    )


def get_download_link(pane_id: str) -> html.A:
    """Get download link component.

    Arguments:
        pane_id: DOM ID of pane.

    Returns:
        HTML component with download link.
    """
    return html.A(
        id=f'{pane_id}-download-link',
        className='download-link',
        download=f'{pane_id}.csv',
        href='',
        target='_blank',
        children=[
            html.Button('Download Data')
        ],
    )


def get_chart_container(pane_id: str, figure=None) -> html.Div:
    """Get chart container component.

    Arguments:
        pane_id: DOM ID of pane.
        figure: Chart figure.

    Returns:
        HTML component with chart container.
    """
    return html.Div(
        id=f'{pane_id}-chart',
        className='chart-container',
        children=[
            dcc.Graph(id=f'{pane_id}-chart-component', figure=figure)
        ]
    )


def get_table_layout(
        pane_id: str,
        controller,
        style_cell: Optional[dict] = None,
        style_cell_conditional: Optional[List[Dict[str, Dict[str, str]]]] = None
) -> html.Div:
    """Get standard layout with common components.

    Arguments:
        pane_id: DOM ID of pane.
        controller: the controller to get data from.
        style_cell: object with default cell style.
        style_cell_conditional: object with conditional cell styles.

    Returns:
        HTML component containing common subcomponents.
    """
    table_columns = controller.get_table_columns()
    table_columns = json.loads(table_columns)['response']['props']['columns']

    table_rows = controller.get_table_rows()
    table_rows = json.loads(table_rows)['response']['props']['data']

    return html.Div(
        id=f'{pane_id}-table',
        children=[
            get_table(pane_id, table_columns, table_rows, style_cell, style_cell_conditional),
            get_download_link(pane_id),
        ]
    )


def get_country_selector(pane_id: str, controller) -> html.Div:
    """Get country selector component.

    Arguments:
        pane_id: DOM ID of pane.

    Returns:
        HTML component with country selector.
    """
    country_options = controller.get_country_options()
    country_options = json.loads(country_options)['response']['props']['options']

    return html.Div(
        id=f'{pane_id}-country-selector',
        className='country-selector',
        children=[
            dcc.Dropdown(
                id=f'{pane_id}-country-selector-dropdown',
                clearable=False,
                options=country_options,
                multi=True
            )
        ]
    )


def get_chart_layout(
        pane_id: str,
        controller,
        country_selector: bool = True,
        scale_toggle: bool = False
) -> html.Div:
    """Get standard layout with common components.

    Arguments:
        pane_id: DOM ID of pane.
        controller: The controller to get data from.
        country_selector: Whether or not chart requires country selector dropdown.
        scale_toggle: Whether or not to allow toggling linear/log scale for y-axis.

    Returns:
        HTML component containing common subcomponents.
    """
    figure = controller.get_chart_figure()
    figure = json.loads(figure)['response']['props']['figure']

    components = []

    if scale_toggle:
        components.append(get_scale_toggle(pane_id))

    components.append(get_chart_container(pane_id, figure))

    if country_selector:
        components.append(get_country_selector(pane_id, controller))

    layout = html.Div(
        id=f'{pane_id}-chart',
        children=components
    )
    return layout
