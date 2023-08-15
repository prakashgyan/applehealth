
from dash import html, register_page  #, callback # If you need callbacks, import it here.
import pandas as pd 
import dash_bootstrap_components as dbc

register_page(
    __name__,
    name='Home',
    top_nav=True,
    path='/'
)

data = pd.read_csv("data/health.csv")
total_steps = data['@steps'].sum()


def layout():
    layout = html.Div(
        children = [  
    html.Div(total_steps, className='big_number', id="number123"),
    html.Div("TOTAL STEPS TILL DATE", className='text_below_big_num'),
    html.Div(className='text_below_big_num',
        children =[
            dbc.NavLink(
                            [
                                html.I(className="fa-solid fa-chevron-down fa-beat-fade fa-lg"),  # Font Awesome Icon
                                " "  # Text beside icon
                            ],
                            href="steps_summary",
                            target="_blank"
                        )
        ])
                ])
    return layout