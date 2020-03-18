import dash_html_components as html

from views.translations import localize


layout = html.Div(
    id="summary-dashboard",
    children=[
        # html.H4(localize('summary-welcome')),
        # html.P(localize('summary-intro')),
        # html.P(localize('summary-description')),
        html.H4(id='summary-welcome'),
        html.P(id='summary-intro'),
        html.P(id='summary-description'),
        html.P(
            children=[
                # html.Span(localize('data-credit')),
                html.Span(id='data-credit'),
                html.A(
                    'Johns Hopkins CSSE',
                    href='https://systems.jhu.edu/',
                    target='_blank'
                ),
                # html.Span(localize('data-update')),
                html.Span(id='data-update'),
            ]
        ),
        html.P(
            children=[
                # html.Span(localize('geoip-credit')),
                html.Span(id='geoip-credit'),
                html.A(
                    'MaxMind',
                    href='https://dev.maxmind.com/geoip/geoip2/geolite2/',
                    target='_blank'
                ),
            ]
        ),
        html.Div(id='detected-country', style={'display': 'None'})
    ]
)

