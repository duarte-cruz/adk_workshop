import os
from dotenv import load_dotenv

# --- Importações do ADK ---
from google.adk.agents import Agent
from google.adk.tools import google_search

load_dotenv()

# Verificação simples (bom para debugging)
if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("GEMINI_API_KEY não encontrada. Define-a no ficheiro .env")
if not os.getenv("GOOGLE_API_KEY") or not os.getenv("GOOGLE_CSE_ID"):
    print("Aviso: Chaves do Google Search não encontradas. A ferramenta de pesquisa irá falhar.")
1
#TODO: Define AGENT_INSTRUCTION with the instruction promopt of the agent.
AGENT_INSTRUCTION = """
TODO: Add the instruction prompt for the ScholarAgent here.
"""
root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction=AGENT_INSTRUCTION,
    #TODO: Add google_search tool: https://google.github.io/adk-docs/tools/built-in-tools/#google-search
)
