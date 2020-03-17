import dash_core_components as dcc
import dash_html_components as html


header = html.Div(
    id='header',
    children=[
        dcc.Store(id='local', storage_type='local'),
        html.Div(children=[
            html.Div(
                children=[
                    html.H1(
                        id='covid-19-dashboard',
                        children=['COVID-19 Data Dashboard']
                    ),
                ],
                className='header-section'
            ),
            html.Div(
                children=[
                    html.A(
                        href='https://systems.jhu.edu/',
                        children=['Data by JHU CSSE'],
                        target='_blank'
                    ),
                ],
                id='credit',
                className='header-section'
            ),
        ]),
    ]
)
