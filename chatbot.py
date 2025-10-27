import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import SQLDatabaseChain
from langchain.sql_database import SQLDatabase

# 🔐 Charger la clé API Gemini depuis .env ou les secrets Streamlit Cloud
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 🧠 Initialiser le modèle Gemini
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

# 🗃️ Connexion à la base SQLite
db = SQLDatabase.from_uri("sqlite:///database.db")

# 🔗 Créer la chaîne d'interrogation SQL via LangChain
chain = SQLDatabaseChain.from_llm(llm=llm, database=db, verbose=False)

# 💬 Fonction d'interrogation
def interroger_chatbot(question):
    try:
        return chain.run(question)
    except Exception as e:
        return f"Erreur lors de l'interrogation : {str(e)}"


