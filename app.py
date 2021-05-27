# -*- coding: utf-8 -*-

# import libraries

import pandas as pd 
import plotly.express as px 


df_2015=pd.read_csv('icnf_2015.csv')


# Plot Map 

# asssign to fig a map graph using our dataframe values

fig = px.scatter_mapbox(df_2015, lat="LAT", lon="LON",
                color="AREATOTAL", size="AREATOTAL",
                color_continuous_scale=px.colors.sequential.Oranges, 
                size_max=50, zoom=4,
                mapbox_style="carto-darkmatter",
                title="Incêndios em Portugal por Área Ardida - 2015")


# show map on screen

fig.show()

