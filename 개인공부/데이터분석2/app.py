import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df1 = pd.read_csv(
    'C:/Users/BAUM/Desktop/multicampus/TIL/개인공부/데이터분석2/result0219.csv')

fig = px.bar(df1, x="지점", y="수량(int)", color="제품타입")

app.layout = html.Div(children=[
    html.H1(children='Dsah Board'),

    html.Div(children='''
        작업 대쉬 보드 
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
