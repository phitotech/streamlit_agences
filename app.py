
import streamlit as st
import sqlite3
from chatbot import interroger_chatbot
import os
from dotenv import load_dotenv

st.sidebar.header("🔧 Diagnostic système")

# Vérification de la clé API
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    st.sidebar.success("✅ Clé Gemini détectée")
else:
    st.sidebar.error("❌ Clé Gemini manquante")

# Vérification de la base de données
try:
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    st.sidebar.success(f"✅ Base de données connectée ({len(tables)} tables)")
except Exception as e:
    st.sidebar.error(f"❌ Erreur DB : {str(e)}")

# Test rapide du chatbot
test_question = st.sidebar.text_input("💬 Test rapide du chatbot", "Quels sont les thèmes disponibles ?")
if st.sidebar.button("Tester le chatbot"):
    try:
        from chatbot import interroger_chatbot
        reponse = interroger_chatbot(test_question)
        st.sidebar.write("Réponse du chatbot :")
        st.sidebar.write(reponse)
    except Exception as e:
        st.sidebar.error(f"❌ Erreur chatbot : {str(e)}")

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
