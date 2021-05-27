# icnf_mapas
Map of forest fires by burnt area in Portugal 

# Requirements 

pandas==1.2.4

plotly==4.14.3

plotly-express==0.4.1


# Functions 

The scripts: 
- Sends a query to ICNF's web service, treats the data, and saves a .csv file locally
- read a CSV file and makes a scatter plot based on the burnt area 


# Data source 

## [ICNF](https://fogos.icnf.pt/localizador/webserviceocorrencias.asp?ano=2015) 


# Files 

**xmlretriver.py** - this script allows you to query the asp.net server to gather the data you need. 
After getting the data the script saves a .csv file locally that you can use with the **app.py** script. 

**app.py** - reads the csv file and plots the map 

**An API with the ICNF dataset will be made available soon**

# CONTRIBUTING 

Please read our [contributing.md](https://github.com/vostpt/icnf_mapas/blob/main/contributing.md) file 

# LICENSE

## MIT License

Copyright (c) [2021] [VOST Portugal - Associação de Voluntários Digitais em Situações de Emergência](https://vost.pt)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

