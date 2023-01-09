# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output, State

# Read the spacex data into pandas dataframe
spacex_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv',  encoding = "ISO-8859-1", )





# defining global variables
opts = [{'label': 'ALL', 'value': 'ALL'}, {'label': 'CCAFS LC-40', 'value': 'OPT1'}, {'label': 'VAFB SLC-4E', 'value': 'OPT2'}, {'label': 'KSC LC-39A', 'value': 'OPT3'}, {'label': 'CCAFS SLC-40', 'value': 'OPT4'}]

style_0 = {'width':'80%', 'padding':'3px', 'font-size': '18px', 'text-align-last' : 'center'}
bg_clr = '#f8faf6'

df = spacex_data.groupby(['Launch Site'])['class'].sum().reset_index()

fig = px.pie(df, values='class', names='Launch Site', title='Launch Site Success Rate')
fig_2 = px.scatter(spacex_data, x="Payload Mass (kg)", y="class", color="Booster Version")

# create dash app
app = Dash(__name__)

# Layout
app.layout = html.Div(children=[
    # Title
    html.Div(children=[
        html.H1(children='SpaceX Launch Dashboard',  style={'text-align-last' : 'center', 'padding':'5px'}),
        html.Div([ html.Div(html.Div('Launch Site:',  style={'justify-content' : 'center', 'font-size': '28px', 'align-items':'center',  'padding':'6px'})),
                   dcc.Dropdown(id='drop_down', options=opts, placeholder="Select a Report", style=style_0)
                 ], style={'display':'flex', 'margin': '1.5em', 'justify-content' : 'center', 'align-items':'center'})
                      ]),

        html.Div([ ], id='plot1'),
        html.Div(dcc.RangeSlider(id='range', min=0, max=10000, step=1000, marks={0: '0', 10000: '10000'},),  style={'padding':'5px'}),
        html.Div([ ], id='plot2'),
        
],

 style={'margin': '1.2em', 'backgroundColor':bg_clr })
print(spacex_data.head())


# Define callback function 
@app.callback([Output(component_id='plot1', component_property='children'),
               Output(component_id='plot2', component_property='children')],
               [Input(component_id='drop_down', component_property='value'),
               Input(component_id='range', component_property='value')],
               [State("plot1", 'children'), State("plot2", 'children')])

def get_pie_chart(entered_site, payload_range, children1, children2):
    print(payload_range)
    
    if entered_site == 'ALL':
        filtered_df = spacex_data
        df = filtered_df.groupby(['Launch Site'])['class'].sum().reset_index()
        fig = px.pie(df, values='class', names='Launch Site', title='Launch Site Success Rate')
        df_scatter = filtered_df[(filtered_df["Payload Mass (kg)"]>=payload_range[0])&(filtered_df["Payload Mass (kg)"]<=payload_range[1])]
        fig_2 = px.scatter(df_scatter, x="Payload Mass (kg)", y="class", color="Booster Version")
        return [dcc.Graph(figure=fig), dcc.Graph(figure=fig_2)]
     
    elif entered_site == 'OPT1':
        filtered_df = spacex_data[spacex_data["Launch Site"]=='CCAFS LC-40']
        df = filtered_df.groupby(['Launch Site'])['class'].sum().reset_index()
        fig = px.pie(df, values='class', names='Launch Site', title='Launch Site Success Rate')
        df_scatter = filtered_df[(filtered_df["Payload Mass (kg)"]>=payload_range[0])&(filtered_df["Payload Mass (kg)"]<=payload_range[1])]
        fig_2 = px.scatter(df_scatter, x="Payload Mass (kg)", y="class", color="Booster Version")
        return [dcc.Graph(figure=fig), dcc.Graph(figure=fig_2)]
    elif entered_site == 'OPT2':
        filtered_df = spacex_data[spacex_data["Launch Site"]=='VAFB SLC-4E']
        df = filtered_df.groupby(['Launch Site'])['class'].sum().reset_index()
        fig = px.pie(df, values='class', names='Launch Site', title='Launch Site Success Rate')
        df_scatter = filtered_df[(filtered_df["Payload Mass (kg)"]>=payload_range[0])&(filtered_df["Payload Mass (kg)"]<=payload_range[1])]
        fig_2 = px.scatter(df_scatter, x="Payload Mass (kg)", y="class", color="Booster Version")
        return [dcc.Graph(figure=fig), dcc.Graph(figure=fig_2)]
    elif entered_site == 'OPT3':
        filtered_df = spacex_data[spacex_data["Launch Site"]=='KSC LC-39A']
        df = filtered_df.groupby(['Launch Site'])['class'].sum().reset_index()
        fig = px.pie(df, values='class', names='Launch Site', title='Launch Site Success Rate')
        df_scatter = filtered_df[(filtered_df["Payload Mass (kg)"]>=payload_range[0])&(filtered_df["Payload Mass (kg)"]<=payload_range[1])]
        fig_2 = px.scatter(df_scatter, x="Payload Mass (kg)", y="class", color="Booster Version")
        return [dcc.Graph(figure=fig), dcc.Graph(figure=fig_2)]
    elif entered_site == 'OPT4':
        filtered_df = spacex_data[spacex_data["Launch Site"]=='CCAFS SLC-40']
        df = filtered_df.groupby(['Launch Site'])['class'].sum().reset_index()
        fig = px.pie(df, values='class', names='Launch Site', title='Launch Site Success Rate')
        df_scatter = filtered_df[(filtered_df["Payload Mass (kg)"]>=payload_range[0])&(filtered_df["Payload Mass (kg)"]<=payload_range[1])]
        fig_2 = px.scatter(df_scatter, x="Payload Mass (kg)", y="class", color="Booster Version")
        return [dcc.Graph(figure=fig), dcc.Graph(figure=fig_2)]


if __name__ == '__main__':
    app.run_server(debug=True)
