import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np




st.title("Comparación de casos confirmados de Covid-19 en Argentina")




data_url2= 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
covid_df2 = pd.read_csv(data_url2)
covid_df2= covid_df2.groupby("Country/Region").sum()
lista_de_paises_df =covid_df2.index.values.tolist()

st.title("")
option = st.selectbox(
     'Seleccione un pais a comparar con Argentina?',
    lista_de_paises_df)

st.write('Seleccionaste:', option)


x_arg=covid_df2.loc[ 'Argentina' , : ]
x_rusia = covid_df2.loc[ 'Russia' , : ]
x_canada = covid_df2.loc[ 'Canada' , : ]
x_vietnam = covid_df2.loc[ 'Vietnam' , : ]
x_yemen = covid_df2.loc[ 'Yemen' , : ]
x_mexico = covid_df2.loc[ 'Mexico' , : ]

x_pais_seleccionado = covid_df2.loc[ option , : ]


#df_rusia =covid_df2[covid_df2['Country/Region'].str.contains("Russia", case=True)]
#df_canada =covid_df2[covid_df2['Country/Region'].str.contains("Canada", case=True)]
#df_vietnam =covid_df2[covid_df2['Country/Region'].str.contains("Vietnam", case=True)]
#df_yemen =covid_df2[covid_df2['Country/Region'].str.contains("Yemen", case=True)]
#df_mexico =covid_df2[covid_df2['Country/Region'].str.contains("Mexico", case=True)]

#df_pais_seleccionado=covid_df2[covid_df2['Country/Region'].str.contains(option, case=True)]

#x_arg = df_arg.iloc[0:1, 6:].values
x_arg= x_arg[2:]

#x_rusia = df_rusia.iloc[0:1, 6:].values
x_rusia= x_rusia[2:]

#x_canada = df_canada.iloc[0:1, 6:].values
x_canada= x_canada[2:]

#x_vietnam = df_vietnam.iloc[0:1, 6:].values
x_vietnam= x_vietnam[2:]

#x_yemen = df_yemen.iloc[0:1, 6:].values
x_yemen= x_yemen[2:]

#x_mexico = df_mexico.iloc[0:1, 6:].values
x_mexico= x_mexico[2:]

#x_pais_seleccionado = df_pais_seleccionado.iloc[0:1, 6:].values
x_pais_seleccionado= x_pais_seleccionado[2:]


paises_argentina_con_seleccionado= np.vstack((x_arg,x_pais_seleccionado))
casos_max_argentina_con_seleccionado=[]
for i in range(2):
    casos_max_argentina_con_seleccionado.append(paises_argentina_con_seleccionado[i][-1])



st.header(f"Comparación de Argentina con {option}")
st.markdown("Acumulación de contagios desde el dia 22/01/20 hasta el presente ")
st.markdown("El gráfico representa días transcurridos/cantidad de contagios acumulados")

data = pd.DataFrame({
    'Paises': ['Argentina', option],
    'Casos Max Confirmados Por Paises ': casos_max_argentina_con_seleccionado
,
}) 

#st.write(x_pais_seleccionado)



df = pd.DataFrame({
  'Argentina': np.array(x_arg),
  option: np.array(x_pais_seleccionado),
},index=np.linspace(0,len(x_arg),len(x_arg)))
#el index no hace falta
st.line_chart(df)


#data1=pd.DataFrame(data1).transpose()
#data1 = data1.set_axis(['Rusia', 'Argentina', 'Canadá',"Vietnam","Yemen","México"], axis=1, inplace=False)

#data1.index.names = ['dias']




st.title("")
st.markdown("Información de los países")

st.write(data)
st.title("")
st.markdown(f"Total de contagios acumulados de Argentina y {option} desde el dia 22/01/20 hasta el presente")


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

st.write("Información de los países")
st.write(data)
st.markdown("Total de contagios acumulados por país desde el dia 22/01/20 hasta el presente ")

st.write(alt.Chart(data).mark_bar().encode(
    x=alt.X('Paises', sort=None),
    y='Casos Max Confirmados Por Paises ',
).properties(width=700, height=500))


st.title("")

st.header("Comparación de varios países elegidos")

COUNTRIES = lista_de_paises_df
COUNTRIES_SELECTED = st.multiselect('Selecciones los países a comparar (Mínimo dos)', COUNTRIES)

#covid_df2 = pd.read_csv(data_url2)
#COUNTRIES_SELECTED.append("Argentina")
lista_paises_seleccionados = None

for pais in COUNTRIES_SELECTED:
    x_pais = covid_df2.loc[ pais , : ]
    x_pais= x_pais[2:]
    #x_pais = df_pais.iloc[0:1, 6:].values
    #x_pais= x_pais[0]
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
    st.markdown("Información de los países seleccionados")
    st.write(data)
    st.markdown("Total de contagios acumulados por país desde el dia 22/01/20 hasta el presente ")
    st.write(alt.Chart(data).mark_bar().encode(
        x=alt.X('Paises', sort=None),
        y='Casos Max Confirmados Por Paises ',
    ).properties(width=700, height=500))


    st.markdown("Contagios acumulados de Covid-19  desde el dia 22/01/20 hasta el presente ")
    st.markdown("El gráfico representa días transcurridos/cantidad de contagios acumulados")

    chart_data = pd.DataFrame(
        lista_paises_seleccionados.transpose(),
        columns=COUNTRIES_SELECTED)

    st.line_chart(chart_data)



 



st.write("Creado por Pértile Franco Giuliano")
st.markdown("https://github.com/francofgp/streamlit-Casos-Covid-19-Argentina")

