# imports
import dash
from dash import dcc, html 
from dash.dependencies import Input, Output, State 
import pandas as pd
import plotly_express as px
import dash_bootstrap_components as dbc
from whitenoise import WhiteNoise


#Csv imports for Brief 1 
product_region = pd.read_csv('csvs_clean/brief_1_quantity_per_product_per_region.csv', index_col=[0])
prod_cat_region = pd.read_csv('csvs_clean/brief_1_quant_per_prod_cat_per_region.csv', index_col=[0])

#Csv read for Brief 2
perform_region = pd.read_csv('csvs_clean/brief_2_performance_per_region.csv', index_col=[0])

#Csv for Brief 3 
sales_hour_df = pd.read_csv('csvs_clean/brief_3_hour_sales_branches.csv', index_col=[0])

#Csv for Brief 4 
profitability_per_branch_df = pd.read_csv('csvs_clean/brief_4_profitability_per_branch.csv', index_col=[0])
 
# variables from csv data to save for region and branch list 
grouped_region_list = prod_cat_region['region'].drop_duplicates().tolist()
grouped_branches = profitability_per_branch_df['branch_name'].drop_duplicates().tolist()

#Setup
app =  dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP], title='Dashboard Retail Information' )
server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root='assets/')

app.layout = html.Div([
    html.H1('Retail Regional Dashboard'),
    html.Br(),
    html.Br(),# Layout for Brief 1
    html.H2('The Best or Worst Product and Product Categories'),
    html.Br(),
    html.Div(
    [
        dbc.Alert(
            [
                html.I(className='bi bi-info-circle-fill me-2'),
                'Use the Dropdown Menus to make a selection then click the Show Graph button to see the data',
            ],
            color='info',
            className='d-flex align-items-center',
        ),
    ],
    ),
    dcc.Dropdown(
        placeholder ='Select the Best or Worst results',
        options=[{'label': 'Top', 'value': 'top'},
                {'label': 'Bottom', 'value': 'bottom'}],
        id='top-bot-products-dd',
        ),
    dcc.Dropdown(
        placeholder ='Select Products or Product Categories',
        options=[{'label': 'Products', 'value': 'Products'},
                {'label': 'Product Category', 'value': 'Category'}],
        id='products-product-category-dd',
        ),
    dcc.Dropdown(
        placeholder ='Select a Region',
        options=[{'label': i, 'value': i} for i in grouped_region_list],
        id='region-dropdown',
        ),
    html.Br(),
    html.Div(
    [
        dbc.Button(
            'Click to Show Graph', id='plot-graph-btn', className='me-2', n_clicks=0
        ),
        html.Span(id='example-output', style={"verticalAlign": "middle"}),
    ]
    ),
    html.Br(),
    html.Br(),
    html.Div([
    dcc.Graph(id='region-best-worst-products', figure={})]),
    html.Br(), 
    html.Br(), # Layout for Brief 2
    html.H2('The Best or Worst Performing Branches'),
    html.Br(),
    html.Div(
    [
        dbc.Alert(
            [
                html.I(className='bi bi-info-circle-fill me-2'),
                'Use the Dropdown Menus to make a selection then click the Show Graph button to see the data',
            ],
            color='info',
            className='d-flex align-items-center',
        ),
    ],
    ),
    dcc.Dropdown(
        placeholder ='Select the Best or Worst results',
        options=[{'label': 'Top', 'value': 'top'},
                {'label': 'Bottom', 'value': 'bottom'}],
        id='top-bot-performance-dd',
        ),
    dcc.Dropdown(
        placeholder ='Select a Region',
        options=[{'label': i, 'value': i} for i in grouped_region_list],
        id='region-performance-dropdown',
        ),
    html.Br(),
    html.Div(
    [
        dbc.Button(
            'Click to Show Graph', id="plot-graph-btn2", className="me-2", n_clicks=0
        ),
        html.Span(id="example-output2", style={"verticalAlign": "middle"}),
    ]
    ),
    html.Br(),
    html.Br(),
    html.Div([
    dcc.Graph(id='region-best-worst-performance', figure={})]),
    html.Br(),
    html.Br(), # Layout for Brief 3 
    html.H2('The Hourly Sales Data for the Top Ten Performing Branches'),
    html.Br(),
        html.Div(
    [
        dbc.Alert(
            [
                html.I(className='bi bi-info-circle-fill me-2'),
                'Use the Dropdown Menus to make a selection then click the Show Graph button to see the data',
            ],
            color='info',
            className='d-flex align-items-center',
        ),
    ],
    ),
    dcc.Dropdown(
        placeholder ='Select a Region',
        options=[{'label': i, 'value': i} for i in grouped_region_list],
        id='region-sales-dropdown',
        ),
    dcc.Dropdown(
        placeholder ='Select the Year to visualise',
        options= [
        { 'label': '2010', 'value': 2010},
        { 'label': '2011', 'value': 2011},
        { 'label': '2012', 'value': 2012},
        { 'label': '2013', 'value': 2013},
        { 'label': '2014', 'value': 2014},
        { 'label': '2015', 'value': 2015},        
        { 'label': '2016', 'value': 2016},
        { 'label': '2017', 'value': 2017},
        { 'label': '2018', 'value': 2018},        
        { 'label': '2019', 'value': 2019},
        { 'label': '2020', 'value': 2020}
        ], 
        id='year-sales-dd',
        ),
    dcc.Dropdown(
        options=[
        { 'label': 'January', 'value': 1},
        { 'label': 'February', 'value': 2},
        { 'label': 'March', 'value': 3},
        { 'label': 'April', 'value': 4},
        { 'label': 'May', 'value': 5},
        { 'label': 'June', 'value':6},        
        { 'label': 'July', 'value': 7},
        { 'label': 'August', 'value': 8},
        { 'label': 'September', 'value': 9},        
        { 'label': 'October', 'value': 10},
        { 'label': 'November', 'value': 11},
        { 'label': 'December', 'value': 12}
        ],
        id='month-sales-dd',
        ),
    html.Br(),
     html.Div(
    [
        dbc.Button(
            'Click to Show Graph', id="plot-graph-btn3", className="me-2", n_clicks=0
        ),
        html.Span(id="example-output3", style={"verticalAlign": "middle"}),
    ]
    ),
    html.Br(),
    html.Br(),
    html.Div([
    dcc.Graph(id='sales-hour-performance', figure={})]),
    html.Br(),
    html.Br(), # Layout for Brief 4
    html.H2('Profitability for the Ten Best or Worst Performing Branches'),
    html.Br(),
            html.Div(
    [
        dbc.Alert(
            [
                html.I(className='bi bi-info-circle-fill me-2'),
                'Use the Dropdown Menu to make a selection then click the Show Graph button to see the data',
            ],
            color='info',
            className='d-flex align-items-center',
        ),
    ],
    ),
    dcc.Dropdown(
        placeholder ='Select the Best or Worst results',
        options=[{'label': 'Top', 'value': 'top'},
                {'label': 'Bottom', 'value': 'bottom'}],
        id='top-bot-profitability-dd',
        ),
    html.Br(),
    html.Div(
    [
        dbc.Button(
            'Click to Show Graph', id="plot-graph-btn4", className="me-2", n_clicks=0
        ),
        html.Span(id="example-output4", style={"verticalAlign": "middle"}),
    ]
    ),
    html.Br(),
    html.Br(),
    html.Div([
    dcc.Graph(id='best-worst-profitability', figure={})]),
    html.Br()
])


# Callback for Brief 1 to display top or bottom results either Products or Product Category for the selected region from dropdown and plot graph on button click 
@app.callback(
        Output(component_id='region-best-worst-products', component_property='figure'), # Output of graph as figure 
        Input(component_id='plot-graph-btn', component_property='n_clicks'),            # Input from button to display the graph
        State(component_id='top-bot-products-dd', component_property='value'),          # State - selection of top or bottom values from dropdown without callback initiated
        State(component_id='products-product-category-dd', component_property='value'), # Dropdown of Products or Category 
        State(component_id='region-dropdown', component_property='value'),              # Dropdown for region 
 )

#input in first provided as option to request the Products or Category data
def request_products(button_click, top_bot, prod_prod_cat, selected_region):
    if [top_bot, prod_prod_cat, selected_region] is not None:
        if top_bot == 'top':
            if prod_prod_cat == 'Products':    
                region_selected = product_region[product_region['region'] == selected_region].head()
                figure = px.bar(region_selected, x='product', y='quantity', color='product', title=f'The Regional Top Five - Products for {selected_region}' )
                return figure 
            else: 
                region_selected = prod_cat_region[prod_cat_region['region'] == selected_region].head()
                figure = px.bar(region_selected, x='category', y='quantity', color='category', title=f'The Regional Top Five - Category for {selected_region}' )
                return figure
        else:
            if prod_prod_cat == 'Products':    
                region_selected = product_region[product_region['region'] == selected_region].tail()
                figure = px.bar(region_selected, x='product', y='quantity', color='product', title=f'The Regional Bottom Five - Products for {selected_region}' )
                return figure 
            else: 
                region_selected = prod_cat_region[prod_cat_region['region'] == selected_region].tail()
                figure = px.bar(region_selected, x='category', y='quantity', color='category', title=f'The Regional Bottom Five - Category for {selected_region}' )
                return figure        
    else:
        return {}

# Callback for Brief 2 to see the top performance and display graph with performance and information about sales and quantity       
@app.callback(
    Output(component_id='region-best-worst-performance', component_property='figure'),
    Input(component_id='plot-graph-btn2', component_property='n_clicks'),  # graph for brief 2 
    State(component_id='top-bot-performance-dd', component_property='value'),  # dropdown for top or bottom fields for performance display
    State(component_id='region-performance-dropdown', component_property='value'), # dropdown for regions for the performance graph
    
)
# showing the top ten or top bottom branches for the selected region 
def show_performance( button_click, top_bot, selected_region):
    if [top_bot,  selected_region] is not None:
        if top_bot == 'top':
            branch_selected = perform_region[perform_region['region'] == selected_region].head(10) 
            figure = px.bar(branch_selected, x='branch_name', y='performance', color='performance', title=f'The Regional Top Ten - Performing Branches for the Region of {selected_region}', hover_data=['amount_in_gbp', 'performance', 'quantity'] )
            return figure 
        else: 
            branch_selected = perform_region[perform_region['region'] == selected_region].tail(10)
            figure = px.bar(branch_selected, x='branch_name', y='performance', color='performance', title=f'The Regional Bottom Ten - Performing Branches for the Region of {selected_region}', hover_data=['amount_in_gbp', 'performance', 'quantity'] ) 
            return figure     
    else:
        return {}

#app callback for brief 3 
@app.callback(
    Output(component_id='sales-hour-performance', component_property='figure'),
    Input(component_id='plot-graph-btn3', component_property='n_clicks'),
    State(component_id='region-sales-dropdown', component_property='value'), 
    State(component_id='year-sales-dd', component_property='value'), 
    State(component_id='month-sales-dd', component_property='value'), 
)

# in test took out argument of date picker selected_datetime
def sales_graph( button_click, selected_region, year_dd, month_dd):
    if [ selected_region, year_dd, month_dd] is not None:
            branch_selected = perform_region[perform_region['region'] == selected_region].head(10) # selection from the brief 2 csv displaying top 10 for selected region
            value_list = branch_selected['branch_name'].values.tolist()
            sales_df = pd.read_csv('csvs_clean/brief_3_hour_sales_branches.csv', index_col=[0])
            # first filter and iteration to ensure only the top ten representing branch_selected is filtered from the full hourly sales df of all branches
            sales_df_filtered = sales_df[sales_df['branch_name'].isin(value_list) ]
            # second iteration 
            sales_df_filtered_by_year = sales_df_filtered[sales_df_filtered['year'] == year_dd]
            # third iteration 
            sales_df_filtered_by_month = sales_df_filtered_by_year[sales_df_filtered_by_year['month'] == month_dd].sort_values(by ='hour')
            
            figure = px.line(sales_df_filtered_by_month, x='hour', y='amount_in_gbp', color='branch_name', title=f'The Regional Top Ten - Hourly Sales for Branches within the Region of {selected_region}', hover_data=['amount_in_gbp'], markers=True )
            return figure 
    else:
        return {}

#Brief 4 callback 
@app.callback(
    Output(component_id='best-worst-profitability', component_property='figure'),
    Input(component_id='plot-graph-btn4', component_property='n_clicks'),
    State(component_id='top-bot-profitability-dd', component_property='value'), 
)

def profitability_graph(button_click, top_bot):    
    if [top_bot] is not None:
        if top_bot == 'top':
            branch_profit = profitability_per_branch_df.head(10) 
            figure = px.pie(branch_profit, values='profitability', names='branch_name', title=f'The Ten Most Profitable Branches', hover_data=['profitability'] )
            return figure 
        else: 
            branch_profit = profitability_per_branch_df.tail(10)          
            figure = px.pie(branch_profit, values='profitability', names='branch_name', title=f'The Ten Least Profitable Branches', hover_data=['profitability'] )
            return figure     
    else:
        return {}

if __name__ == '__main__':
    app.run_server(debug=True)
