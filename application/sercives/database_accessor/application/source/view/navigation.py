from dash import html as dash_html

from application.sercives.navigation_bar import navigation_bar

navigation_bar = (
    dash_html.Div(
        [
            navigation_bar,
        ],
    ),
)
