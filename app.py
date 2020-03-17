import dash

external_stylesheets = [
    # 'https://s3.amazonaws.com/crase-scoring-dashboard/css/plotly.css',
    # 'https://s3.amazonaws.com/crase-scoring-dashboard/css/dashboard.css',
    # 'https://codepen.io/chriddyp/pen/dZVMbK.css',
    'static/plotly.css',
    'static/dashboard.css',
    'https://fonts.googleapis.com/css?family=Montserrat:300,300i,400,400i,500,500i,600,600i,700,700i',
    'https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i',
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
# app.script.config.serve_locally = True
