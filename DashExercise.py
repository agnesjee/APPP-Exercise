
# Exercise 20: Setup the environment
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
df = pd.read_csv('USA_Housing.csv')

# Exercise 19: Create a table
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
            ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                ]) for i in range(min(len(dataframe), max_rows))
            ])
        ])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Exercise 21: Create dropdown box that contains all the addresses
app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(id='dropdown', options=[
            {'label': i, 'value': i} for i in df.Address.unique()
            ], multi=True, placeholder='Filter by address...'),
    html.Div(id='table-container')
])

@app.callback(
    dash.dependencies.Output('table-container', 'children'),
    [dash.dependencies.Input('dropdown', 'value')])
def display_table(dropdown_value):
    if dropdown_value is None:
        return generate_table(df)

    dff = df[df.Address.str.contains('|'.join(dropdown_value))]
    return generate_table(dff)


if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    
    
