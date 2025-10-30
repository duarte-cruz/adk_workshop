import os
from dotenv import load_dotenv

# --- ADK imports ---
from google.adk.agents import Agent

load_dotenv()

# Simple checks (useful for debugging)
if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("GEMINI_API_KEY not found. Set it in the .env file")
if not os.getenv("GOOGLE_API_KEY") or not os.getenv("GOOGLE_CSE_ID"):
    raise ValueError("Google Search keys not found. The search tool will fail.")

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
