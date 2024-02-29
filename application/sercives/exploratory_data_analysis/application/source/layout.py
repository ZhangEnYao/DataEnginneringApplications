from dash_bootstrap_components import NavbarSimple, NavItem, NavLink, Row, Container
from dash.html import Div, H3

navigation_bar = NavbarSimple(
    children=[
        NavItem(
            NavLink("Logout", href="/authority/logout", external_link=True)
        ),
    ],
    brand="Application Center",
    brand_href='/',
    brand_external_link=True,
    fluid = True,
    color="light",
)

layout = Div(
    [
        Container(
            [
                Row(
                    navigation_bar
                ),
                Row(
                    H3('Exploratory Data Analysis')
                ),
            ]
        )
    ]
)