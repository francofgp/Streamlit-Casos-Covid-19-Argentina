import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np




st.title("Comparación de casos confirmados de Covid-19 en Argentina")

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
st.markdown("Acumulación de contagios desde el dia Cero")
data = pd.DataFrame({
    'Paises': ['Argentina', option],
    'Casos Max Confirmados Por Paises ': casos_max_argentina_con_seleccionado
,
})

#st.write(x_pais_seleccionado)

df = pd.DataFrame({
  'Argentina': x_arg,
  option: x_pais_seleccionado
})


st.line_chart(df)


#data1=pd.DataFrame(data1).transpose()
#data1 = data1.set_axis(['Rusia', 'Argentina', 'Canadá',"Vietnam","Yemen","México"], axis=1, inplace=False)

#data1.index.names = ['dias']




st.title("")
st.write(data)
st.title("")

st.write(alt.Chart(data).mark_bar().encode(
    x=alt.X('Paises', sort=None),
    y='Casos Max Confirmados Por Paises ',
).properties(width=700, height=500))



paises = np.vstack((x_rusia,x_arg))
paises = np.vstack((paises,x_canada))
paises = np.vstack((paises,x_vietnam))
paises = np.vstack((paises,x_yemen))
paises = np.vstack((paises,x_mexico))
data1=paises

casos_max_por_paises=[]
for i in range(6):
    casos_max_por_paises.append(paises[i][-1])

#casos_max_por_paises


st.title("")

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


st.title("")

st.header("Comparación de varios países elegidos")

COUNTRIES = ['Argentina','Russia',"US", 'Canada',"Bolivia","Brazil","Ecuador","Italy","Israel","Jamaica","India", 'Vietnam',"Yemen","Mexico","Angola","Armenia","Iran","Iraq","Indonesia","Saudi Arabia","Tanzania","Togo"]
COUNTRIES_SELECTED = st.multiselect('Selecciones los países a comparar (Mínimo dos)', COUNTRIES)

covid_df2 = pd.read_csv(data_url2)
#COUNTRIES_SELECTED.append("Argentina")
lista_paises_seleccionados = None

for pais in COUNTRIES_SELECTED:
    df_pais = covid_df2[covid_df2['Country/Region'].str.contains(pais, case=True)]
    x_pais = df_pais.iloc[0:1, 6:].values
    x_pais= x_pais[0]
    if lista_paises_seleccionados is None:
        lista_paises_seleccionados=x_pais
    else:
        lista_paises_seleccionados = np.vstack((lista_paises_seleccionados,x_pais))


    
if len(COUNTRIES_SELECTED)>=2:

    casos_max_por_paises=[]
    for i in range(len(COUNTRIES_SELECTED)):
        casos_max_por_paises.append(lista_paises_seleccionados[i][-1])
        


    data = pd.DataFrame({
        'Paises': COUNTRIES_SELECTED,
        'Casos Max Confirmados Por Paises ': casos_max_por_paises
    ,
    })
    print(casos_max_por_paises)

    st.write(data)
    st.write(alt.Chart(data).mark_bar().encode(
        x=alt.X('Paises', sort=None),
        y='Casos Max Confirmados Por Paises ',
    ).properties(width=700, height=500))



    st.write("Creado por Pértile Franco Giuliano")
    st.markdown("https://github.com/francofgp/streamlit-Casos-Covid-19-Argentina")


 
