from dash import html, dcc, register_page, callback , Input, Output # If you need callbacks, import it here.
import pandas as pd 
import dash_bootstrap_components as dbc
import plotly.express as px

register_page(
    __name__,
    name='distance_summary',
    top_nav=True,
    path='/distance_summary'
)

data = pd.read_csv("data/health.csv")
data.drop("Unnamed: 0", axis=1, inplace=True)
data.rename(columns={"@startDate":"Timeline","@walkHours":"walkHours","@kms":'kms',"@steps":"steps","@walkMins":"walkMins"}, inplace= True)
data["Timeline"] = data.Timeline.astype('datetime64[ns]')

# fig = px.bar(data, x="Timeline", y="kms")
# fig.update_layout(plot_bgcolor="white")
# fig.update_traces(line_color = "#ff1919")

def layout():
    layout = html.Div(
        children = [  
        html.Div(className='full_page_graph',
            children = [
            html.Div("Your distance trend", className='text_below_big_num', id="number123"),
            dcc.Dropdown(["Daily","Monthly","Yearly"], id='dropdown_group', value="Daily"),
            dcc.Graph(
                id='example-graph',
                figure=draw_graph(data)),
            html.Div(className='text_below_big_num',
                children =[
                    dbc.NavLink(
                                    [
                                        html.I(className="fa-solid fa-chevron-down fa-beat-fade fa-lg"),  # Font Awesome Icon
                                        " "  # Text beside icon
                                    ],
                                    href="distance_summary",
                                    target="_blank"
                                )])
                        ])
                ])
    return layout


@callback(
    Output('example-graph', 'figure'),
    Input('dropdown_group', 'value'),
)
def update_graph(value,):
    if value is None or value == "Daily":
        return draw_graph(data)
    elif value == "Monthly":
        return draw_graph(data.resample("M", on="Timeline").sum().reset_index())
    elif value == "Yearly":
        return draw_graph(data.resample("Y", on="Timeline").sum().reset_index())
    # return 'The input value was "{}" and the button has been clicked times'.format(value)


def draw_graph(data):
    fig = px.bar(data, x="Timeline", y="kms")
    fig.update_layout(plot_bgcolor="white")
    return fig
