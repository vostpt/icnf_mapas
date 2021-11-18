# -*- coding: utf-8 -*-

# Import libraries 

import pandas as pd 
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Read CSV to a pandas datafrane

df = pd.read_csv('icnf_2015_raw.csv')

#Create a new Dataframe that sums total burned area by District

new_df = df.groupby(["ANO","DISTRITO"]).AREATOTAL.sum().reset_index()

# Pivot the dataframe for heatmap

amatrix = new_df.pivot("ANO", "DISTRITO", "AREATOTAL")

# Create heatmap with a fixed scale

sns.heatmap(amatrix,cmap="rocket_r",vmin=0, vmax=20000)

# Show plot 

plt.show()


# Close Python console to end script 


