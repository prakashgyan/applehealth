from dash import html, dcc, register_page  #, callback # If you need callbacks, import it here.
import pandas as pd 
import dash_bootstrap_components as dbc
import plotly.express as px

register_page(
    __name__,
    name='steps_summary',
    top_nav=True,
    path='/steps_summary'
)

data = pd.read_csv("data/health.csv")
data.drop("Unnamed: 0", axis=1, inplace=True)
data.rename(columns={"@startDate":"startDate","@walkHours":"walkHours","@kms":'kms',"@steps":"steps","@walkMins":"walkMins"}, inplace= True)
data["startDate"] = data.startDate.astype('datetime64[ns]')

fig = px.line(data, x="startDate", y="steps")
fig.update_layout(plot_bgcolor="white")
fig.update_traces(line_color = "#ff1919")

def layout():
    layout = html.Div(
        children = [  
        html.Div(className='full_page_graph',
            children = [
            html.Div("Your steps trend", className='text_below_big_num', id="number123"),
            dcc.Graph(
                id='example-graph',
                figure=fig),
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