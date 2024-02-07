
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import dash
import dash_core_components as dcc
import dash_html_components as html
# Create the Dash application, make sure to adjust requests_pathname_prefx
app_dash = dash.Dash(__name__, requests_pathname_prefix='/dash/')
app_dash.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5],
                    'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

# Now create your regular FASTAPI application

app = FastAPI()

@app.get("/hello_fastapi")
def read_main():
    return {"message": "Hello World"}

# Now mount you dash server into main fastapi application
app.mount("/dash", WSGIMiddleware(app_dash.server))
