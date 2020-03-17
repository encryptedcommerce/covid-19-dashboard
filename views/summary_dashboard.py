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
        html.P('This dashboard contains interactive visualization of COVID-19 data.'),
        html.P(description),
        html.P(
            children=[
                html.Span('Data is provided by '),
                html.A(
                    'Johns Hopkins CSSE',
                    href='https://systems.jhu.edu/',
                    target='_blank'
                ),
                html.Span(', updated daily around 00:05 UTC'),
            ]
        ),
        html.P(
            children=[
                html.Span('Geographic / IP data is provided by '),
                html.A(
                    'MaxMind',
                    href='https://dev.maxmind.com/geoip/geoip2/geolite2/',
                    target='_blank'
                ),
                html.Span(', used for including your country in the default selection.'),
            ]
        )
    ]
)

