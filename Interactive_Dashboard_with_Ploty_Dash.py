#importing required lib

import pandas as pd
import dash
from dash import dcc
import das_html_components as html
from dash.dependicies import Input, Output
import plotly.express as px

#Step1 : Read data from csv into pandas dataframe
csvdata_df = pd.read_csv("spacex_launch_dash.csv")

#Step2 : Create a Dash application
app = dash.Dash(__name__)

#Step3 : Create a Dash app layout
app.layout = html.Div(children= [html.H1('Interactive Dashboard'),style={'textAlign' : "center' , 'color' = '#000080', 'font-size':45}),
                                  #Step4 : Create a Dropdown list of available data options
                                  #Step5 : Connect a graph - pie chart to the dropdown choice
                                  #Step6 : Create a slider 
                                  #Step7 : Create a graph - scatter plot to displat slider range 
                                ]
                       )

#Step4 : Create a Dropdown list of available data options
#Step5 : Connect a graph - pie chart to the dropdown choice
#Step6 : Create a slider 
#Step7 : Create a graph - scatter plot to displat slider range 
