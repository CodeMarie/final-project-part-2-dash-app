# imports
# from msilib.schema import Component
import dash
from dash import dcc, html 
from dash.dependencies import Input, Output, State 
import pandas as pd
import plotly_express as px



# csv imports for Brief 1 
product_region = pd.read_csv('csvs_clean/brief_1_quantity_per_product_per_region.csv', index_col=[0])
prod_cat_region = pd.read_csv('csvs_clean/brief_1_quant_per_prod_cat_per_region.csv', index_col=[0])

#Csv read for Brief 2
perform_region = pd.read_csv('csvs_clean/brief_2_performance_per_region.csv', index_col=[0])

#Csv for Brief 3 
sales_hour_df = pd.read_csv('csvs_clean/brief_3_hour_sales_branches.csv', index_col=[0])

#Csv for Brief 4 
profitability_per_branch_df = pd.read_csv('csvs_clean/brief_4_profitability_per_branch.csv', index_col=[0])

# variables from csv data 
grouped_region_list = prod_cat_region['region'].drop_duplicates().tolist()


# setup
app =  dash.Dash(__name__, title='Dashboard Retail Information')
# server = app.server

df1 = pd.read_csv('csvs_clean/brief_1_quantity_per_product_per_region.csv')

app.layout = html.Div([
    html.H1('Retail Regional Dashboard'),
    html.Br(),
    html.Br(),
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
    html.Br(),
    html.Button('Click to Show Graph', id='plot-graph-btn', n_clicks=0),
    html.Br(),
    html.Br(),
    html.Div([
    dcc.Graph(id='region-best-worst-products', figure={})]),
    html.Br(), 
    html.Br(),
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
    html.Br(),
    html.Button('Click to Show Graph', id='plot-graph-btn2', n_clicks=0),
    html.Br(),
    html.Br(),
    html.Div([
    dcc.Graph(id='region-best-worst-performance', figure={})]),
    html.Br(),
    html.Br(),

    html.Br(), # Layout for Brief 3 
        dcc.Dropdown(
        placeholder ='Select a Region',
        options=[{'label': i, 'value': i} for i in grouped_region_list],
        id='region-sales-dropdown',
        ),
        dcc.Dropdown(
        placeholder ='Select the Year to visualise',
        options= {
        '2010': '2010',
        '2011': '2011',
        '2012': '2012',
        '2013': '2013',
        '2014': '2014',
        '2015': '2015',
        '2016': '2016',
        '2017': '2017',
        '2018': '2018',
        '2019': '2019',
        '2020': '2020',
        }, 
        value='2020',
        id='year-sales-dd',
        ),
    # dcc.DatePickerSingle(
    #     date='2020-01-01',
    #     display_format='MMM DD YYYY', 
    #     id='date-picker'
    # ),
    html.Br(),
    html.Br(),
    html.Div([
    # dcc.RangeSlider( 
    #    marks={ 
    #             0: '12am',     # key=position, value=what is shown {'label': '5', 'style':  'font-weight':'bold'}},
    #             1: '1am',
    #             2: '2am',
    #             3: '3am',
    #             4: '4am',
    #             5: '5am',
    #             6: '6am',
    #             7: '7am',
    #             8: '8am',
    #             9: '9am',
    #             10: '10am',
    #             11: '11am',
    #             12: '12pm',
    #             13: '1pm',
    #             14: '2pm',
    #             15: '3pm',
    #             16: '4pm',
    #             17: '5pm',
    #             18: '6pm',
    #             19: '7pm',
    #             20: '8pm',
    #             21: '9pm',
    #             22: '10pm',
    #             23: '11pm'
    #             },
    #         step=1, min=0, max=23, value=[0, 1], id='hour-range-slider', tooltip = { 'always_visible': True }, updatemode='drag'),
    # html.Div(id='output-container-range-slider'),
    html.Br(),
    html.Button('Click to Show Graph', id='plot-graph-btn3', n_clicks=0),
    dcc.Graph(id='sales-hour-performance', figure={})]),
    html.Br(),
    html.Br(),
    ])


# Callback for Brief 1 to display top or bottom results either Products or Product Category for the selected region from dropdown and plot graph on button click 
@app.callback(
        Output(component_id='region-best-worst-products', component_property='figure'),
        Input(component_id='plot-graph-btn', component_property='n_clicks'),
        State(component_id='top-bot-products-dd', component_property='value'),
        State(component_id='products-product-category-dd', component_property='value'),
        State(component_id='region-dropdown', component_property='value'),
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
            branch_selected = perform_region[perform_region['region'] == selected_region].head(10) # selection from the brief 2 csv displaying top 10 for selected region
            figure = px.bar(branch_selected, x='branch_name', y='performance', color='performance', title=f'The Regional Top Ten - Performing Branches for the Region of {selected_region}', hover_data=['amount_in_gbp', 'performance', 'quantity'] )
            print(branch_selected)
            return figure 
        else: 
            branch_selected = perform_region[perform_region['region'] == selected_region].tail(10)
            figure = px.bar(branch_selected, x='branch_name', y='performance', color='performance', title=f'The Regional Bottom Ten - Performing Branches for the Region of {selected_region}', hover_data=['amount_in_gbp', 'performance', 'quantity'] )
            print(branch_selected) 
            return figure     
    else:
        return {}

#app callback for brief 3 
@app.callback(
    Output(component_id='sales-hour-performance', component_property='figure'),
    # Output(component_id='output-container-range-slider', component_property='children'),
    Input(component_id='plot-graph-btn3', component_property='n_clicks'),
    # State(component_id='top-bot-sales-dd', component_property='value'),  # dropdown for top or bottom fields for performance display
    # Input(component_id='hour-range-slider', component_property='value'),
    # State(component_id='date-picker', component_property='date')
    State(component_id='region-sales-dropdown', component_property='value'), # dropdown for regions for the performance graph
    State(component_id='year-sales-dd', component_property='value'), # dropdown for Year for the performance graph
)

# in test took out argument of date picker selected_datetime
def sales_graph( button_click, selected_region):
    # if selected_datetime is not None :
        # return f'Selected Date: {selected_datetime}',
    if [ selected_region] is not None:
        # if top_bot == 'top':
            branch_selected = perform_region[perform_region['region'] == selected_region].head(10) # selection from the brief 2 csv displaying top 10 for selected region
            # print(branch_selected['branch_name']) 
            value_list = branch_selected['branch_name'].values.tolist()
            print(value_list) 
            sales_df = pd.read_csv('csvs_clean/brief_3_hour_sales_branches.csv', index_col=[0])


            # first filter and iteration
            sales_df_filtered = sales_df[sales_df['branch_name'].isin(value_list) ]
            # second iteration 
            sales_df_filtered_by_year = sales_df_filtered[sales_df_filtered['year'] == 2012]
            # third iteration 
            sales_df_filtered_by_month = sales_df_filtered_by_year[sales_df_filtered_by_year['month'] == 1].sort_values(by ='hour')
            
            figure = px.line(sales_df_filtered_by_month, x='hour', y='amount_in_gbp', color='branch_name', title=f'The Regional Top Ten - Hourly Sales for Branches within the Region of {selected_region}', hover_data=['amount_in_gbp'] )
            return figure 
    else:
        return {}



#run ensures we dont try to run the app using both gunicorn and flasks in built server
if __name__ == '__main__':
    app.run_server(debug=True)
