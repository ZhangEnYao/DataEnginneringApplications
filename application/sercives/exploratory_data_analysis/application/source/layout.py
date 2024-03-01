from dash.html import H3, Div
from dash_bootstrap_components import (Container, NavbarSimple, NavItem,
                                       NavLink, Row)

navigation_bar = NavbarSimple(
    children=[
        NavItem(
            NavLink("Logout", href="/authority/logout", external_link=True)
        ),
    ],
    brand="Application Center",
    brand_href='/',
    brand_external_link=True,
    fluid=True,
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
