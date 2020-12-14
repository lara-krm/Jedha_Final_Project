import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import plotly.express as px


# Suppress_callback_exceptions will avoid raising warnings when using multiple callbacks
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX], suppress_callback_exceptions=True)

df = pd.read_csv("apps/csv_needed/eda_instacart.csv")
df1 = pd.read_csv("apps/csv_needed/graph01.csv") 
df2a = pd.read_csv("apps/csv_needed/graph02a.csv")
df2b = pd.read_csv("apps/csv_needed/graph02b.csv")
df3 = pd.read_csv("apps/csv_needed/df_count_total.csv")
df4 = pd.read_csv("apps/csv_needed/df_group1_dash.csv")
df5 = pd.read_csv("apps/csv_needed/df_group3_dash.csv")
df7 = pd.read_csv("apps/csv_needed/df_results_group1.csv")
df8 = pd.read_csv("apps/csv_needed/df_results_group3.csv")

users_grp1=['44334', '195996', '185616', '185262', '35106', '31665', '88016', '172234', '158455', '142694']
users_grp3=['15105', '64472', '37050', '45570', '89576', '100069', '85323', '191739', '159402', '102438']

fig1 = go.Figure(
    data = go.Bar(x=df1["product_name"], 
             y=df1["counts"], 
                  marker={'color': df1["counts"],
            'colorscale': 'plasma'}, showlegend = False),
    layout = go.Layout(
        title = go.layout.Title(text = "Number of produts ordered", x = 0.5),
        xaxis = go.layout.XAxis(title = 'Products')
    )
)

fig2 = make_subplots(2,1, subplot_titles=('Products bought in each day of the week',
                                        'Products bought in each hour of the day'))

fig2.add_trace(go.Bar(x=['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 
             y=df2a["counts"], 
            marker={'color': df2a["counts"],
            'colorscale': 'plasma'}, showlegend = False),
              row=1, col=1)
fig2.add_trace(go.Bar(x=df2b["order_hour_of_day"], 
             y=df2b["counts"], marker={'color': df2b["counts"],
            'colorscale': 'plasma'}, showlegend = False)
              , row=2, col=1)

fig2.layout.annotations[0].update(font= {'size': 9})
fig2.layout.annotations[1].update(font= {'size': 9})
fig2['layout']['xaxis']['title']='Day of week'
fig2['layout']['xaxis2']['title']='Hour of the day'
fig2['layout']['yaxis']['title']='Count'
fig2['layout']['yaxis2']['title']='Count'

fig2.update_layout(height=700)

fig3 = px.histogram(df3, x="total_count")
fig3.update_layout(title_text='Distribution of users\'s purchases', title_x = 0.5)  

fig9 = go.Figure(data=[
    go.Bar(name='Total Product', x=users_grp1, y=df7.loc[df7["Algo"]=="ALS", :].total_count.to_list(),\
          #marker_color='lightsalmon', opacity=0.75
          ),
    go.Bar(name='Unique Product', x=users_grp1, y=df7.loc[df7["Algo"]=="ALS", :].unique_count.to_list(),\
          #marker_color='#330C73', opacity=0.75
          )
])
# Change the bar mode
fig9.update_layout(barmode='group', xaxis_type='category', 
                  title_text='Total product bought vs Unique product bought per user, Group 1')

fig12 = go.Figure(data=[
    go.Bar(name='Total Product', x=users_grp3, y=df8.loc[df8["Algo"]=="ALS", :].total_count.to_list(),\
          #marker_color='lightsalmon', opacity=0.75
          ),
    go.Bar(name='Unique Product', x=users_grp3, y=df8.loc[df8["Algo"]=="ALS", :].unique_count.to_list(),\
          #marker_color='#330C73', opacity=0.75
          )
])
# Change the bar mode
fig12.update_layout(barmode='group', xaxis_type='category', 
                  title_text='Total product bought vs Unique product bought per user, Group 3')

layout = html.Div(
    dbc.Container([

        dbc.Row([
            dbc.Col(html.H1("EDA for INSTACART"), className="mb-2")
        ]),

        html.Div(style={'padding': 50}),

        dash_table.DataTable(
            id='datatable',
            fixed_rows={'headers': True},
            page_action='none',
            style_table={'height': 300, 'overflowY': 'scroll', 'overflowX': 'scroll', 'padding' : 10},
            style_header={'backgroundColor': '#25597f', 'color': 'white'},
            style_cell={
                'backgroundColor': 'white',
                'color': 'black',
                'fontSize': 13,
                'font-family': 'Nunito Sans',
                'minWidth': 95, 'maxWidth': 95, 'width': 95},
            columns=[{"name" : i, "id" : i} for i in df.columns],
            data=df.to_dict('records')
        ),

        html.Div(style={'padding': 50}),

        dbc.Row([
            dbc.Col(dbc.Card(dbc.CardHeader('Data Visualization on the total dataset',
                                     className="text-center text-light bg-dark"), 
                                     #body=True, 
                                     color="dark"))
        ], className="mb-4"),

        dbc.Row([
            dbc.Col(dbc.Card([dbc.CardHeader("GRAPH NB 1"),
                dbc.CardBody([
                dcc.Graph(id="example-graph-1", figure=fig1)]),
                ], color="light"))
        ]),

        html.Div(style={'padding': 30}),

        dbc.Row([
            dbc.Col(dbc.Card([dbc.CardHeader("GRAPH NB 2"),
                dbc.CardBody([
                dcc.Graph(id="example-graph-2", figure=fig2)]),
                ], color="light"))
        ]),

        html.Div(style={'padding': 30}),

        dbc.Row([
            dbc.Col(dbc.Card([dbc.CardHeader("GRAPH NB 3"),
                dbc.CardBody([
                dcc.Graph(id="example-graph-3", figure=fig3)]),
                ], color="light"))
        ]),

        html.Div(style={'padding': 50}),

        dbc.Row([
            dbc.Col(dbc.Card(dbc.CardHeader('Split datasets for further analysis',
                                     className="text-center text-light bg-dark"), 
                                     #body=True, 
                                     color="dark"))
        ], className="mb-4"),

        dbc.Row([
            dbc.Col(dbc.Card([dbc.CardHeader("Users behavior, based on historical purchases"),
                dbc.CardBody([
                        dcc.Graph(id="example-graph-9", figure=fig9),
                        dcc.Graph(id="example-graph-12", figure=fig12)
                ]),
            ], color="light"
            ))
        ]),

#        dbc.Row([
#            dbc.Col(
#            dash_table.DataTable(
#           id='datatable2',
#            fixed_rows={'headers': True},
#            page_action='none',
#            style_table={'height': 300, 'overflowY': 'scroll', 'overflowX': 'scroll', 'padding' : 10},
#            style_header={'backgroundColor': '#25597f', 'color': 'white'},
#            style_cell={
#                'backgroundColor': 'white',
#                'color': 'black',
#                'fontSize': 9,
#                'font-family': 'Nunito Sans',
#                'minWidth': 55, 'maxWidth': 55, 'width': 55},
#            columns=[{"name" : i, "id" : i} for i in df4.columns],
#            data=df4.to_dict('records')
#            )),
#
#           dbc.Col(
#            dash_table.DataTable(
#            id='datatable3',
#            fixed_rows={'headers': True},
#            page_action='none',
#            style_table={'height': 300, 'overflowY': 'scroll', 'overflowX': 'scroll', 'padding' : 10},
#            style_header={'backgroundColor': '#25597f', 'color': 'white'},
#            style_cell={
#                'backgroundColor': 'white',
#                'color': 'black',
#                'fontSize': 9,
#                'font-family': 'Nunito Sans',
#                'minWidth': 55, 'maxWidth': 55, 'width': 55},
#            columns=[{"name" : i, "id" : i} for i in df5.columns],
#            data=df5.to_dict('records')
#        ))
#        ])

    ])
)
    

#if __name__ == '__main__':
#    app.run_server(debug=True)


