import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# import all pages in the app
from apps import eda_graphs, algo_model, home
from app import app 
from app import server

# make a reuseable navitem for the different examples
#nav_item = dbc.NavItem(dbc.NavLink("Link", href="#"))


# building the navigation bar
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/home"),
        dbc.DropdownMenuItem("EDA", href="/eda_graphs"),
        dbc.DropdownMenuItem("Algo", href="/algo_model"),
    ],
    nav = True,
    in_navbar = True,
    label = "Explore",
)

# this is the default navbar style created by the NavbarSimple component
#navbar = dbc.NavbarSimple(
#    children=[dropdown],
#    brand="FULLSTACK Final Project",
#    brand_href="/home",
#    sticky="top",
#    className="mb-5",
#)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand("FULLSTACK Final Project", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/eda_graphs':
        return eda_graphs.layout
    elif pathname == '/algo_model':
        return algo_model.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)