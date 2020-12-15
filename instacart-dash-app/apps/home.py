import dash
import dash_html_components as html
import dash_bootstrap_components as dbc


#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX], suppress_callback_exceptions=True)

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Welcome to the INSTACART dashboard", className="text-center")
                    , className="mb-5 mt-5")
        ]),

        #html.A(
        dbc.Row([
            html.H5(["We are proud to present you, our work on the ", 
            html.A('Instacart Kaggle Dataset!', href="https://www.kaggle.com/c/instacart-market-basket-analysis")], 
            className="ml-2") #mb-4
        ],no_gutters=True),

        html.Div(style={'padding': 20}),

        dbc.Row([
            dbc.Col(html.H5("Our dataset :") #, className="text-center")
                    , className="ml-2", width = 2),
            dbc.Col(html.Img(src="assets/dataset2.png", style={'width': "600px", 'height': "400px"}), width=6)
            ], justify="start")
    ])
])

#if __name__ == '__main__':
#    app.run_server(debug=True)