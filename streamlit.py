import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np





st.title("Comparación de casos confirmados de Covid-19 de Argentina")

st.title("")
option = st.selectbox(
     'Seleccione un pais a comparar con Argentina?',
    ('Russia',"US", 'Canada',"Bolivia","Brazil","Ecuador","Italy","Israel","Jamaica","India", 'Vietnam',"Yemen","Mexico","Angola","Armenia","Iran","Iraq","Indonesia","Saudi Arabia","Tanzania","Togo"))

st.write('Seleccionaste:', option)


data_url2= 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
covid_df2 = pd.read_csv(data_url2)
df_arg = covid_df2[covid_df2['Country/Region'].str.contains("Argentina", case=True)]
df_rusia =covid_df2[covid_df2['Country/Region'].str.contains("Russia", case=True)]
df_canada =covid_df2[covid_df2['Country/Region'].str.contains("Canada", case=True)]
df_vietnam =covid_df2[covid_df2['Country/Region'].str.contains("Vietnam", case=True)]
df_yemen =covid_df2[covid_df2['Country/Region'].str.contains("Yemen", case=True)]
df_mexico =covid_df2[covid_df2['Country/Region'].str.contains("Mexico", case=True)]

df_pais_seleccionado=covid_df2[covid_df2['Country/Region'].str.contains(option, case=True)]

x_arg = df_arg.iloc[0:1, 6:].values
x_arg= x_arg[0]

x_rusia = df_rusia.iloc[0:1, 6:].values
x_rusia= x_rusia[0]

x_canada = df_canada.iloc[0:1, 6:].values
x_canada= x_canada[0]

x_vietnam = df_vietnam.iloc[0:1, 6:].values
x_vietnam= x_vietnam[0]

x_yemen = df_yemen.iloc[0:1, 6:].values
x_yemen= x_yemen[0]

x_mexico = df_mexico.iloc[0:1, 6:].values
x_mexico= x_mexico[0]

x_pais_seleccionado = df_pais_seleccionado.iloc[0:1, 6:].values
x_pais_seleccionado= x_pais_seleccionado[0]


paises_argentina_con_seleccionado= np.vstack((x_arg,x_pais_seleccionado))
casos_max_argentina_con_seleccionado=[]
for i in range(2):
    casos_max_argentina_con_seleccionado.append(paises_argentina_con_seleccionado[i][-1])

st.header(f"Comparación de Argentina con {option}")
data = pd.DataFrame({
    'Paises': ['Argentina', option],
    'Casos Max Confirmados Por Paises ': casos_max_argentina_con_seleccionado
,
})

st.write(data)
st.write(alt.Chart(data).mark_bar().encode(
    x=alt.X('Paises', sort=None),
    y='Casos Max Confirmados Por Paises ',
).properties(width=700, height=500))



paises = np.vstack((x_rusia,x_arg))
paises = np.vstack((paises,x_canada))
paises = np.vstack((paises,x_vietnam))
paises = np.vstack((paises,x_yemen))
paises = np.vstack((paises,x_mexico))

casos_max_por_paises=[]
for i in range(6):
    casos_max_por_paises.append(paises[i][-1])

#casos_max_por_paises



st.header("Comparación de varios países con argentina")
data = pd.DataFrame({
    'Paises': ['Rusia', 'Argentina', 'Canadá',"Vietnam","Yemen","México"],
    'Casos Max Confirmados Por Paises ': casos_max_por_paises
,
})

st.write(data)
st.write(alt.Chart(data).mark_bar().encode(
    x=alt.X('Paises', sort=None),
    y='Casos Max Confirmados Por Paises ',
).properties(width=700, height=500))


st.write("Creado por Pértile Franco Giuliano")