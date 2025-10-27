
import streamlit as st
import sqlite3
from chatbot import interroger_chatbot

st.title("Exploration des données internationales")

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

theme = st.selectbox("Choisissez un thème", ["Économie", "Santé", "Éducation"])
region = st.selectbox("Choisissez une région", ["Afrique", "Asie", "Europe", "Amériques"])

query = f"SELECT * FROM sources WHERE theme='{theme}' AND region='{region}'"
results = cursor.execute(query).fetchall()

st.write("Résultats :")
for row in results:
    st.write(row)

question = st.text_input("Posez une question sur les données :")
if question:
    reponse = interroger_chatbot(question)
    st.write(reponse)
