import pandas as pd
import plotly.express as px
from urllib.request import urlopen
import json

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv("Surprise.csv",dtype={"FIPS_Code": str})
#df.head()

fig = px.choropleth(df, geojson=counties, locations='FIPS_Code', color="Unemployed_Rate",
                           hover_name = 'Area_name',
                           color_continuous_scale="oranges",
                           range_color=(0, 6),
                           scope="usa",
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

fig1 = px.choropleth(df, geojson=counties, locations='FIPS_Code', color="Bachelors_Rate",
                           hover_name = 'Area_name',
                           color_continuous_scale="oranges",
                           range_color=(0, 20),
                           scope="usa",
                           labels={'bach':'Bachlors rate'}
                          )
fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig1.show()

fig2 = px.choropleth(df, geojson=counties, locations='FIPS_Code', color="Surprise",
                           hover_name = 'Area_name',
                           color_continuous_scale="oranges",
                           range_color=(0, 30),
                           scope="usa",
                           labels={'surprise':'Surprise rate'}
                          )
fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig2.show()