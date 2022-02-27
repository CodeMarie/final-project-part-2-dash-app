# imports
import dash
from dash import dcc, html 
from dash.dependencies import Input, Output 

# test dictionary
region_dict = {

1: 'East of England',
2: 'East Midlands',
3: 'London',
4: 'North East England',
5:  'Northern Ireland',
6:  'North West England',
7: 'Scotland',
8: 'South East England',
9:  'South West England',
10: 'Wales',
11: 'West Midlands',
12: 'Yorkshire and the Humber',
}


# setup
app =  dash.Dash(__name__, title='Dashboard Retail Information')
server = app.server

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id='region-dropdown',
        options=[
            {'label': l, 'value': v}
            for v, l in region_dict.items()
        ],
        value=list(region_dict.keys())[0]
    ),
 html.Div(id='region-dd-output-container')
])


@app.callback(
    #callback for region dropdown
    Output('region-dd-output-container', 'children'), 
    Input('region-dropdown', 'value'))

# function to display region 
def display_output(value):
    return f'You have selected "{value}"'


#run ensures we dont try to run the app using both gunicorn and flasks in built server
if __name__ == '__main__':
    app.run_server(debug=True)
