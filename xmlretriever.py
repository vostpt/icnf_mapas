# -*- coding: utf-8 -*-

# With thanks to https://stackoverflow.com/users/6792743/perl 

# import libraries

import pandas as pd 
import requests
import xml.etree.ElementTree as ET
import io
from io import StringIO  
import plotly.express as px 


# XML Query 

# Get data
resp = requests.get(
    'https://fogos.icnf.pt/localizador/webserviceocorrencias.asp?ano=2015')

# Parse XML
et = ET.parse(io.StringIO(resp.text))

# Create DataFrame
df = pd.DataFrame([
    {f.tag: f.text for f in e.findall('./')} for e in et.findall('./')]
)

# Change Columns Types 

df["LON"] = pd.to_numeric(df["LON"])
df["LAT"] = pd.to_numeric(df["LAT"])
df["AREATOTAL"] = pd.to_numeric(df["AREATOTAL"])

# Save to CSV 

df.to_csv("icnf_2015.csv")


