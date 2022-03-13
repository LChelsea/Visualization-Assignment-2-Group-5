import pandas as pd
import plotly.express as px
from urllib.request import urlopen
import json

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv("Surprise.csv",dtype={"FIPS_Code": str})
#df.head()

fig1 = px.choropleth(df, geojson=counties, locations='FIPS_Code', color= "Expected_Unemployment_Rate",
                           hover_name = 'Area_name',
                           color_continuous_scale="tealrose",
                           range_color=(0, 6),
                           scope="usa",
                           labels={'unemp':'unemployment rate'}
                          )
fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig1.show()

fig2 = px.choropleth(df, geojson=counties, locations='FIPS_Code', color= "Unemployment_rate_2000",
                           hover_name = 'Area_name',
                           color_continuous_scale="tealrose",
                           range_color=(-8, 8),
                           scope="usa",
                           labels={'unemp':'unemployment rate'}
                          )
fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig2.show()

fig3 = px.choropleth(df, geojson=counties, locations='FIPS_Code', color= "Unemployment_Surprise",
                           hover_name = 'Area_name',
                           color_continuous_scale="tealrose",
                           range_color=(-8, 8),
                           scope="usa",
                           labels={'unemp':'unemployment rate'}
                          )
fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig3.show()