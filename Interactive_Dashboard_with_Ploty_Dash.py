#importing required lib

import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px


#Step1 : Read data from csv into pandas dataframe
csvdata_df = pd.read_csv("spacex_launch_dash.csv")
#print(csvdata_df.head(5))
max_payload = csvdata_df['Payload Mass (kg)'].max()
min_payload = csvdata_df['Payload Mass (kg)'].min()

#Step2 : Create a Dash application
app = dash.Dash(__name__)


#Step3 : Create a Dash app layout
app.layout = html.Div(children= [html.H1('Interactive Dashboard',style={'textAlign' : 'center' , 'color' : '#000080', 'font-size':45}),
                                  #Step4 : Create a Dropdown list of available data options
                                  #provide list options and a value to be sent callback to
                                  dcc.Dropdown(options=[
                                                     {'label': 'All Sites', 'value': 'ALL'},
                                                     {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                                     {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                                     {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                                     {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
                                                     ], value = 'All', id='dropdown'),

                                  html.Br(),
                                  #Step5 : Connect a graph - pie chart to the dropdown choice
                                  html.H1('Interactive pie chart with Dropdown',style={'textAlign' : 'center' , 'color' : '#000080', 'font-size':30}),
                                  #placeholder to plot selected from dropdown list
                                  html.Div(dcc.Graph(id='graph-pie-chart')),
                                  html.Br(),

                                  #Step6 : Create a slider 
                                   html.H1('Interactive scatterplot with slider',style={'textAlign' : 'center' , 'color' : '#000080', 'font-size':30}),
                                   #dcc.Slider(min=0, max=20, step=5, value=10, id='my-slider')
                                  #dcc.Slider(min = min_payload, max = max_payload, step = 1000, value = max_payload, id='slider')

                                  #dcc.RangeSlider(min=0, max=20, step=1, value=[5, 15], id='my-range-slider'),
                                  dcc.RangeSlider(min=min_payload, max=max_payload, step=1000, value=[min_payload, max_payload], id='slider'),


                                  #Step7 : Create a graph - scatter plot to displat slider range 
                                 
                                  #placeholder to plot selected from dropdown list
                                  html.Div(dcc.Graph(id='graph-scatter-plot')),
                                  html.Br(),
                                  
                                ]
                       )

#code yet to be refined for proper rendering 


#Step4 : callback to render data from Create a Dropdown list of available data options
#Step5 : callback to render data to Connect a graph - pie chart to the dropdown choice
@app.callback(Output(component_id='graph-pie-chart', component_property='figure'),
              Input(component_id='dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = csvdata_df
    if entered_site == 'ALL':
        fig = px.pie(filtered_df, values='class', 
        names='Launch Site', 
        title='Success Count for all launch sites')
        return fig
    else:
        # return the outcomes piechart for a selected site
        filtered_df=spacex_df[csvdata_df['Launch Site']== entered_site]
        filtered_df=filtered_df.groupby(['Launch Site','class']).size().reset_index(name='class count')
        fig=px.pie(filtered_df,values='class count',names='class',title=f"Total Success Launches for site {entered_site}")
        return fig


#Step6 : callback to render data from Create a slider 
#Step7 : callback to render data toCreate a graph - scatter plot to displat slider range 
@app.callback(Output(component_id='graph-scatter-plot',component_property='figure'),
                [Input(component_id='dropdown',component_property='value'),
                Input(component_id='slider',component_property='value')])
def scatter(entered_site,payload):
    filtered_df = spacex_df[spacex_df['Payload Mass (kg)'].between(payload[0],payload[1])]
    # thought reusing filtered_df may cause issues, but tried it out of curiosity and it seems to be working fine
    
    if entered_site=='ALL':
        fig=px.scatter(filtered_df,x='Payload Mass (kg)',y='class',color='Booster Version Category',title='Success count on Payload mass for all sites')
        return fig
    else:
        fig=px.scatter(filtered_df[filtered_df['Launch Site']==entered_site],x='Payload Mass (kg)',y='class',color='Booster Version Category',title=f"Success count on Payload mass for site {entered_site}")
        return fig


        
# Run the app
if __name__ == '__main__':
    app.run_server()
