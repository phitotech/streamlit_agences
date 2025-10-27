import os
from langchain.llms import GoogleGenerativeAI
from langchain.chains import SQLDatabaseChain
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
db = SQLDatabase.from_uri("sqlite:///database.db")
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent_executor = initialize_agent(
    tools=toolkit.get_tools(),
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False
)

def interroger_chatbot(question):
    return agent_executor.run(question)

