import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Setup
app = dash.Dash(__name__)

df = pd.read_csv('iris.csv')

fig = px.scatter(df, x="SepalWidthCm", y="SepalLengthCm", color="Species",
                 size='PetalLengthCm', hover_data=['PetalWidthCm'])

# Structure of the Site
app.layout = html.Div([
    html.H1('JF-DashApp'),

    html.Div('Eine Beispielanwendung.'),

        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='xaxis-column',
                    options=[{'label': i, 'value': i} for i in df.columns],
                    value='SepalWidthCm'
                )
            ], style={'width': '48%', 'display': 'inline-block'}),

            html.Div([
                dcc.Dropdown(
                    id='yaxis-column',
                    options=[{'label': i, 'value': i} for i in df.columns],
                    value='SepalLengthCm'
                )
            ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
        ]),

    dcc.Graph(
        id='iris-graph',
        figure=fig
    ),

    html.Div([
        "Name: ",
        dcc.Input(id='name_label_input', value='XY', type='text')
    ]),
    html.Div(
        id='name_label_output'
    )
])

# Callback for updating label
@app.callback(
    Output(component_id='name_label_output', component_property='children'),
    Input(component_id='name_label_input', component_property='value')
)
def update_name_div(input_value):
    return '{} war hier.'.format(input_value)

# Callback for updating graph
@app.callback(
    Output(component_id='iris-graph', component_property='figure'),
    Input(component_id='xaxis-column', component_property='value'),
    Input(component_id='yaxis-column', component_property='value')
)
def update_iris_graph(xaxis_col, yaxis_col):
    return px.scatter(df, x=xaxis_col, y=yaxis_col, color="Species",
                 size='PetalLengthCm', hover_data=['PetalWidthCm'])


if __name__ == '__main__':
    app.run_server(debug=True)