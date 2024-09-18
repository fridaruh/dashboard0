import pandas as pd
import streamlit as st


st.title('Modelo de evaluación de ingresos')
st.markdown(""" En este proyecto se busca encontrar cuáles son las características
    principales que pueden predecir que una persona gane más o menos de $50 K anuales.""")

dataExploration = st.container()
with dataExploration:
    st.header('Dataset: Ingresos')
    st.text("""Este dataset corresponde a una transformación del set de datos oficial proveniente del
    siguiente set de datos:""")


df = pd.read_csv('https://raw.githubusercontent.com/fridaruh/dashboard_streamlit/master/income.csv')

st.write(df.head())

st.subheader('Distrbuciones:')

distribution_sex = pd.DataFrame(df.sex.value_counts())

st.bar_chart(distribution_sex)

st.text('Con esta gráfica buscamos mostrar la distribución de los datos con respecto al sexo.')

newFeatures = st.container()
with newFeatures:
    st.header('Nuevas variables: ')
    st.text('Demos un vistazo a las principales variables de este dataset: ')

st.markdown('* **first feature:** this is the explanation') 
st.markdown('* **second feature:** another explanation')



st.markdown( """ <style>
 .main {
 background-color: #AF9EC;
}
</style>""", unsafe_allow_html=True )