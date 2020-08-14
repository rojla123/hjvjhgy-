
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import folium 
receiver_email = "nizar.selmi@ensi-uma.tn"
message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["To"] = receiver_email
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import pandas as dp
import sqlite3
from pathlib import Path
import streamlit as st
import time
import datetime
import numpy as np
import pydeck as pdk 
import altair as alt 
from datetime import datetime
st.sidebar.image("a.png")
st.sidebar.success("# ENSI") 
st.sidebar.image("ensi.png")
def load_data():
    data=pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')
    return data
df=load_data()
data=load_data()
a=data[data.continent=="Asia"]
b=a["total_cases"].max()
c=a["total_deaths"].max()
r=data[data.continent=="Europe"]
t=r["total_cases"].max()
u=r["total_deaths"].max()
i=data[data.continent=="Africa"]
o=i["total_cases"].max()
p=i["total_deaths"].max()
q=data[data.continent=="North America"]
s=q["total_cases"].max()
d=q["total_deaths"].max()
f=data[data.continent=="South America"]
g=f["total_cases"].max()
h=f["total_deaths"].max()
st.success("# DATAVIZ")
# Create a list of possible values and multiselect menu with them in it.
COUNTRIES = df['location'].unique()
se = st.sidebar.multiselect('Select countries', COUNTRIES)
mask = df['location'].isin(se)
df=df[mask]
z=df["total_cases"].max()
y=df["total_deaths"].max()
r=list(se)+list(".")+list("png")
st.markdown(f"""
<table>
<tr>
<th>continent</th>
<th>max_of deaths</th>
<th>max_of cases</th>
<tr>
<td  <div style=background-color:#2ECC71   width=300>  EUROPE  </td>
<td <div style=background-color:#2ECC71>{u}</td>
<td <div style=background-color:#2ECC71 width=300  >{t}</td>
</tr>
<tr>
<td  <div style=background-color:#2ECC71  width=300   >  ASIA  </td>
<td <div style=background-color:#2ECC71 width=300>  {c}</td>
<td <div style=background-color:#2ECC71>{b}</td>
</tr>
<tr>
<td  <div style=background-color:#2ECC71 width=300>  North Americe </td>
<td <div style=background-color:#2ECC71>{d}</td>
<td <div style=background-color:#2ECC71>{s}</td>
</tr>
<tr>
<td  <div style=background-color:#2ECC71 width=300>  SOUTH AMERICE  </td>
<td <div style=background-color:#2ECC71>{h}</td>
<td <div style=background-color:#2ECC71>{g}</td>
</tr>
<tr>
<td  <div style=background-color:#2ECC71  width=300 >  AFRIQUE  </td>
<td <div style=background-color:#2ECC71>{p}</td>
<td <div style=background-color:#2ECC71>{o}</td>
</tr>
</table> 
<h2   style=background-color:#f5f5dc width=300  height=200   >repartition covid 19 dans le monde</h2>
    <p>Europe</p>
          <div class="w3-light-grey w3-round-xlarge w3-small">
            <div class="w3-container w3-center w3-round-xlarge w3-teal" style="width:80%">
              <div class="w3-center w3-text-white" >63%</div>
            </div>
          </div>
          <p>Africa</p>
          <div class="w3-light-grey w3-round-xlarge w3-small">
            <div class="w3-container w3-center w3-round-xlarge w3-teal" style="width:44%">
              <div class="w3-center w3-text-white" >52%</div>
            </div>
          </div>
          <p>Asia</p>
          <div class="w3-light-grey w3-round-xlarge w3-small">
            <div class="w3-container w3-center w3-round-xlarge w3-teal" style="width:55%">
              <div class="w3-center w3-text-white" >61.1%</div>
            </div>
          </div>
          <p>South America</p>
          <div class="w3-light-grey w3-round-xlarge w3-small">
            <div class="w3-container w3-center w3-round-xlarge w3-teal" style="width:88%">
              <div class="w3-center w3-text-white" >60%</div>
            </div>
          </div>      
          <p>North America</p>
          <div class="w3-light-grey w3-round-xlarge w3-small">
            <div class="w3-container w3-center w3-round-xlarge w3-teal" style="width:89%">
              <div class="w3-center w3-text-white" >65.5%</div>
            </div>
          </div>
         
  """, unsafe_allow_html=True)
f=px.pie(
data_frame=data,
values="total_cases",
color="continent",
names="continent",
title="repartition du pandemie_19 dans le monde"
)
st.plotly_chart(f)
st.markdown(f"""
<table>
<tr>
<th>country</th>
<th>max_of deaths</th>
<th>max_of cases</th>
<tr>
<td><div style=background-color:#2ECC71  width=300  height=200    >{se}</td>
<td <div style=background-color:#2ECC71  width=300 height=200   >{y}</td>
<td <div style=background-color:#2ECC71  width=300  height=200 >{z}</td>
</tr>
</table>   
  
""", unsafe_allow_html=True)
metrics =['total_cases','new_cases','total_deaths','new_deaths','total_cases_per_million','new_cases_per_million','total_deaths_per_million','new_deaths_per_million','total_tests','new_tests','total_tests_per_thousand','new_tests_per_thousand']
dell= st.sidebar.selectbox('Covid metric to view', metrics)
if st.sidebar.button("visualiser"):
  fig2 = px.area(df, x='date', y=dell,color='location')
  fig1= px.area(df, x='date', y='total_deaths',color='location')
  st.success(" # l volution de la pandemie_19 dans le monde")
  r= st.plotly_chart(fig2)
  st.success('# l volution de la pandemie_19 dans le monde')
  ts_char= st.plotly_chart(fig1)
sender_email =st.sidebar.text_input("  e_mail ")
password=st.sidebar.text_input(" password")
message["From"] = sender_email
x=st.text_area("your comment")
if st.sidebar.button("envoyer"):
  part1 = MIMEText(x, "plain")
  message.attach(part1)
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
# let's ask the user which column should be used as Index
if dell in metrics:   
    metric_to_show_in_covid_Layer = dell
st.video("https://www.youtube.com/watch?v=QU9tHJ3TSDs")

st.markdown("""
 
<html>
<title>W3.CSS Template</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Roboto'>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.footer 
{
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: black;
  color: white;
  text-align: center;
}
</style>

<div class="footer">
 <h2>Find me in the social media</h2>
<i class="fa fa-facebook-official w3-hover-opacity"></i>
  <i class="fa fa-instagram w3-hover-opacity"></i>
  <i class="fa fa-snapchat w3-hover-opacity"></i>
  <i class="fa fa-pinterest-p w3-hover-opacity"></i>
  <i class="fa fa-twitter w3-hover-opacity"></i>
  <i class="fa fa-linkedin w3-hover-opacity"></i>
  <p>Powered by <a href="https://www.ENSI.com/w3css/default.asp" target="_blank">ENSI</a></p>
</div>
 
 """, unsafe_allow_html=True)
