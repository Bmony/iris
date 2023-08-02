import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

_, col, _ = st.columns([2, 6, 2])
col.header("Streamlit 시각화")

dfiris = sns.load_dataset("iris")
st.write(dfiris.head())
colors = {"setosa":"red", "virginica" : "green", "versicolor" : "blue"}
st.sidebar.title('Iris Species')
selectX = st.selectbox("X:", ['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
''
selecty = st.selectbox("y:", ['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
''
select_species = st.multiselect("유형 선택 (:blue[다중]:)", ['setosa', 'virginica', 'versicolor'])
''
select_Alpha = st.slider('alpha:', 0.1, 1.0, 0.5)

if select_species:
    fig = plt.figure(figsize=(7, 5))
    for species in select_species:
        df = dfiris[dfiris.species == species]
        plt.scatter(df[selectX], df[selecty], color = colors[species], alpha = select_Alpha, label = species)
    plt.legend(loc = 'lower right')
    plt.xlabel(selectX)
    plt.ylabel(selecty)
    plt.title('iris')
    st.pyplot(fig)
