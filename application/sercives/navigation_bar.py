import dash_bootstrap_components

navigation_bar = dash_bootstrap_components.NavbarSimple(
    children=[
        dash_bootstrap_components.NavItem(
            dash_bootstrap_components.NavLink("Logout", href="/authority/logout", external_link=True)
        ),
    ],
    brand="Application Center",
    brand_href='/',
    brand_external_link=True,
    fluid = True,
    color="light",
)