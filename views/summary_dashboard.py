import dash_html_components as html

description = '''
    You may select countries to include in the chart.
    If detected, your country and others with similar statistics will be added by default,
    in addition to several countries with the highest statistics.
'''

layout = html.Div(
    id="summary-dashboard",
    children=[
        html.H4('Welcome to the COVID-19 Interactive Dashboard'),
        html.P('This dashboard contains interactive visualization of COVID - 19 data.'),
        html.Div(description),
        html.Div(children=[
            html.Span('Data is provided by '),
            html.A('Johns Hopkins CSSE', href='https://systems.jhu.edu/'),
            html.Span(', updated daily around 00:05 UTC'),
        ])
    ]
)

