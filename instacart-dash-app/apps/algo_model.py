import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
from numpy.core.fromnumeric import product
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import plotly.express as px
from fuzzywuzzy import fuzz
from app import app 

#If running as single page app instead:
#Suppress_callback_exceptions will avoid raising warnings when using multiple callbacks
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX], suppress_callback_exceptions=True)

#Import the needed CSV to run the algo_model page
df6 = pd.read_csv("apps/csv_needed/als_reco_allUsers_1&3.csv")
df7 = pd.read_csv("apps/csv_needed/df_results_group1.csv")
df8 = pd.read_csv("apps/csv_needed/df_results_group3.csv")
df9 = pd.read_csv("apps/csv_needed/df_prod_orders_train.csv")

#Define list of users we will use to visualize the algorithms' results
users_grp1=['44334', '195996', '185616', '185262', '35106', '31665', '88016', '172234', '158455', '142694']
users_grp3=['15105', '64472', '37050', '45570', '89576', '100069', '85323', '191739', '159402', '102438']

#Define the graphs needed to vizualize the data
fig7 = go.Figure(data=[
    go.Bar(name='ALS', x=users_grp1, y=df7.loc[df7["Algo"]=="ALS", :].equal_prod.to_list(),
          marker_color='lightsalmon', opacity=0.75),
    go.Bar(name='AP_score', x=users_grp1, y=df7.loc[df7["Algo"]=="ALS", :].AP_score.to_list(),
          marker_color='lightslategray', opacity=0.75),
    go.Bar(name='RBM', x=users_grp1, y=df7.loc[df7["Algo"]=="RBM", :].equal_prod.to_list(),
          marker_color='#330C73', opacity=0.75)
])
#Change the bar mode
fig7.update_layout(barmode='group', xaxis_type='category', 
                  title_text='Equal Product Proportion depending the algorithm, Group 1')

fig10 = go.Figure(data=[
    go.Bar(name='ALS', x=users_grp3, y=df8.loc[df8["Algo"]=="ALS", :].equal_prod.to_list(),
          marker_color='lightsalmon', opacity=0.75),
    go.Bar(name='AP_score', x=users_grp3, y=df8.loc[df8["Algo"]=="ALS", :].AP_score.to_list(),
          marker_color='lightslategray', opacity=0.75),
    go.Bar(name='RBM', x=users_grp3, y=df8.loc[df8["Algo"]=="RBM", :].equal_prod.to_list(),
          marker_color='#330C73', opacity=0.75)
])
#Change the bar mode
fig10.update_layout(barmode='group', xaxis_type='category', 
                  title_text='Equal Product Proportion depending the algorithm, Group 3')                 

fig8 = go.Figure(data=[
    go.Bar(name='ALS', x=users_grp1, y=df7.loc[df7["Algo"]=="ALS", :].equal_aisle.to_list(),
          marker_color='lightsalmon', opacity=0.75),
    go.Bar(name='RBM', x=users_grp1, y=df7.loc[df7["Algo"]=="RBM", :].equal_aisle.to_list(),
          marker_color='#330C73', opacity=0.75)
])
#Change the bar mode
fig8.update_layout(barmode='group', xaxis_type='category', 
                  title_text='Equal Aisle Proportion depending the algorithm, Group 1')

fig11 = go.Figure(data=[
    go.Bar(name='ALS', x=users_grp3, y=df8.loc[df8["Algo"]=="ALS", :].equal_aisle.to_list(),
          marker_color='lightsalmon', opacity=0.75),
    go.Bar(name='RBM', x=users_grp3, y=df8.loc[df8["Algo"]=="RBM", :].equal_aisle.to_list(),
          marker_color='#330C73', opacity=0.75)
])
#Change the bar mode
fig11.update_layout(barmode='group', xaxis_type='category', 
                  title_text='Equal Aisle Proportion depending the algorithm, Group 3')

#Define list of unique users in Group1 and Group3
users = df6.user_id.unique().tolist()
#Define list of unique users who did a new purchase
users_train = df9.user_id.unique().tolist()

#Function to get the recommendations for one specific user
def getReco(df, user_id):
    reco = df[df['user_id'] == user_id].product_name.to_list()
    return reco

#First table content:
tab1_content = dbc.Card(
    dbc.CardBody([

        dbc.Row([
            dbc.Col(
                html.Img(
                    src="assets/algo_comparison5.png", style={'width': "1000px", 'height': "800px"}
                ) 
            )
        ]),

        html.Div(style={'padding': 20}),

        dbc.Row([
            dbc.Col(dbc.Card([dbc.CardHeader("Algorithm results, equal product based on historical purchases"),
                dbc.CardBody([
                dcc.Graph(id="example-graph-7", figure=fig7), 
                dcc.Graph(id="example-graph-10", figure=fig10)
                ])
            ], color="light"
            ))
        ]),

        html.Div(style={'padding': 10}),

        dbc.Row([
            dbc.Col(dbc.Card([dbc.CardHeader("Algorithm results, equal aisle based on historical purchases"),
                dbc.CardBody([
                dcc.Graph(id="example-graph-8", figure=fig8),
                dcc.Graph(id="example-graph-11", figure=fig11)
                ])
            ], color="light"
            ))
        ])
    ])
)

#Second table content
tab2_content = dbc.Card(
    dbc.CardBody([

        dbc.Row(
            dbc.Col(html.H5("Equal product based on new purchases"),
                    className="ml-3")
        ),

        html.Div(style={'padding': 20}),

        #Search engine to get the recommendations per ID
        dbc.Row([
            dbc.Col(
                dbc.Input(id="user_id_form", placeholder="Enter an ID...", type="number"), 
                width=4
            ),
            dbc.Col(
                dbc.Button("Search", id="search", color="primary", className="ml-2"),
                width="auto"
            ),
        ],
        no_gutters=True, 
        className="ml-auto flex-nowrap mt-3 mt-md-0",
        align="center"
        ),

        dbc.Row([
            dbc.Col(
                html.P(id='reco_text', children='Enter a valid user_id to get recommendations'),
                width="auto"
            ),

            dbc.Col(
                html.Div(id="products_tags")
            )
        ], 
        className="ml-auto flex-nowrap mt-3"
        ),

        dbc.Row([
            dbc.Col(
                html.P(id='bought_text', children=''),
                width="auto"
            ),

            dbc.Col(
                html.Div(id="bought_tags")
            )
        ], 
        className="ml-auto flex-nowrap mt-3"
        )
    ])
)

#Change to app.layout if running as single page app instead
#Layout of the algo_model page
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H3("Algorithms used for INSTACART", className="text-center")
                    , className="mb-5 mt-5")
        ]),    

        dbc.Tabs([
            dbc.Tab(tab1_content, label="Analysis based on Historical Purchases"),
            dbc.Tab(tab2_content, label="Analysis based on New Purchases")
        ])
    ])
])

#Define the callback for the search engine
@app.callback(
    Output('reco_text', 'children'),
    Output('products_tags', 'children'),
    Output('bought_text', 'children'),
    Output('bought_tags', 'children'),
    [Input('search', 'n_clicks')], [State('user_id_form', 'value')]
)

#Define the outputs for the search engine
def update_output(n_clicks, user_id):
    if user_id in users:
        tags = []
        products = getReco(df6, user_id)
        matchs = []

        if user_id in users_train:
            tags_b = []
            bought = getReco(df9, user_id)
            for b in bought:
                color = 'secondary'
                for p in products :
                    #Use FuzzyWuzzy to visualize string matching
                    if fuzz.partial_ratio(p.lower(),b.lower()) > 70:
                        matchs.append(p)
                        color = 'success'
                tags_b.append(dbc.Button(str(b), color=color, className="ml-1 mb-1", disabled=True, size="sm"))
            bought_product_label = f'Bought products for the user {user_id} are :'
        else:
            tags_b = []
            bought_product_label = f'This user did not make new purchases.'
        
        for p in products :
            if p in matchs:
                color = 'success'
            else :
                color = 'secondary'
            tags.append(dbc.Button(str(p), color=color, className="ml-1 mb-1", disabled=True, size="sm"))

        return f'Recommended products for the user {user_id} are :', tags, bought_product_label, tags_b

    else:
        tags = []
        return 'Enter a valid user_id to get recommendations', tags, '', []

#If running as single page app instead:
#if __name__ == '__main__':
#    app.run_server(debug=True)