import pandas as pd
import plotly.express as px
from dash import Dash, html, Input, Output, dash_table, dcc, callback

df = pd.read_csv('weather.csv')

app = Dash()

app.layout = [
    html.Div(children='Dashboard'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=20)
]

if __name__ == '__main__':
    app.run(debug=True)