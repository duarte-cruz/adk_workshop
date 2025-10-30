# 🏛️ Workshop: Autonomous Agent Engineering with Google ADK

Welcome to the workshop on the Google Agent Development Kit (ADK).

In this session, we'll move past LLM theory and dive into the practice of agent engineering. Our goal is to focus on an agent's "logic" by completing a code skeleton to build a **"ScholarAgent"** – an autonomous AI agent capable of researching academic sources on the web and synthesizing a response.

This repository contains all the material you need:

  * `requirements.txt`: The Python dependencies.
  * `adk_scholar_workshop/agent.py`: The skeleton of our agent, which we will edit.

## 1\. Required Setup (Mandatory)

To ensure our 90 minutes are focused on development, it is **essential** that you arrive at the session with the following setup completed.

### a. Install Python

Make sure you have **Python 3.9 or higher** installed and working in your terminal.
*Suggestion: To better manage your environments, we strongly recommend using [UV](https://github.com/astral-sh/uv) from Astral. The following instructions will assume you are using it.*

### b. Get API Keys (The Most Important Step)

An agent is composed of a "brain" (LLM) and "hands" (Tools). Both require APIs.

**i. Gemini API Key (The "Brain"):**

1.  Visit the [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  Log in and click "Create API key".
3.  **Copy and save this key.**

**ii. Google Search API Keys (The "Hands"):**
This step has 2 parts and is the most complex:

  * **Custom Search Engine ID:**
    1.  Go to the [Programmable Search Engine](https://programmablesearchengine.google.com/) and click "Add".
    2.  Configure it to "Search the entire web". Give it a name (e.g., "ADK Search").
    3.  After creating, click "Edit search engine" -\> "Basic Information" and copy the **"Search engine ID (CSE ID)"**.
  * **API Key:**
    1.  Go to the [Google Cloud Console](https://console.cloud.google.com/apis/library/customsearch.googleapis.com).
    2.  Enable the **"Custom Search API"** for one of your projects.
    3.  Go to "Credentials", click "Create Credentials" -\> "API Key".
    4.  **Copy and save this key.**

-----

## 2\. Project Initialization (Hands-On)

We will start the practical workshop here.

### a. Clone the Repository (If you haven't already)

```bash
# Clone the repository (replace with the correct URL)
git clone https://github.com/duarte-cruz/adk_workshop.git
cd adk_workshop
```

### b. Install Dependencies

1.  Create your virtual environment using `uv`:

    ```bash
    uv venv
    ```

2.  Activate the environment:

      * **Linux/macOS (bash/zsh):**
        ```bash
        source .venv/bin/activate
        ```
      * **Windows (Command Prompt / git bash):**
        ```bash
        .venv\Scripts\activate
        ```
      * **Windows (PowerShell):**
        ```powershell
        .venv\Scripts\Activate.ps1
        ```

3.  Install the dependencies from the `requirements.txt` file using `uv`:

    ```bash
    uv pip install -r requirements.txt
    ```

### c. Create Environment File (.env)

1.  Navigate to the agent's folder:

    ```bash
    cd adk_scholar_workshop
    ```

2.  Inside `adk_scholar_workshop`, create a file named `.env`.

3.  Paste the following content, replacing `[...]` with the keys you obtained in Part 1:

    ```ini
    # File: adk_scholar_workshop/.env

    # Google AI Studio Key
    GEMINI_API_KEY=[YOUR_GEMINI_API_KEY]

    # Google Search API Keys
    GOOGLE_API_KEY=[YOUR_GOOGLE_CLOUD_API_KEY]
    GOOGLE_CSE_ID=[YOUR_CSE_ID]
    ```

-----

## 3\. The Task: Complete the "ScholarAgent"

Your goal is to open the `adk_scholar_workshop/agent.py` file and complete the sections marked with `TODO`.

This is the skeleton you will find:

```python
# adk_scholar_workshop/agent.py
# ... (imports and checks)
    
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
```

### TODO 1: The Instruction (AGENT\_INSTRUCTION)

Replace the `"TODO: ..."` text inside the `AGENT_INSTRUCTION` variable with a detailed, academic-level instruction.

**Instruction Requirements:** The agent must be instructed to:

  * Identify itself as "ScholarAgent", an academic research assistant.
  * Receive a complex topic from the user.
  * Explicitly use the `Google Search` tool (ADK knows this is the name of the `Google Search` tool).
  * Find a minimum of 3 high-quality sources (academic papers, articles, etc.).
  * Extract the main argument from each source.
  * Synthesize all arguments into a final, cohesive response, citing the sources (Title and URL).

### TODO 2: Add the Tool

In the `root_agent` definition, the `tools` parameter is missing. Add the `tools` parameter and pass it the `Google Search` tool (which is already imported).

**Hint:** The final agent definition should look something like this:

```python
root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='ScholarAgent', # <-- Good idea to change the name
    description='A research agent that finds and synthesizes sources.', # <-- And the description
    instruction=AGENT_INSTRUCTION,
    tools=[google_search] # <-- Your solution for TODO 2
)
```

-----

## 4\. Run and Test

When you are confident with your changes to `agent.py`, save the file.

1.  Make sure you are in the terminal inside the repo root folder:
    ```bash
    # (If you are in the folder `adk_scholar_workshop`, run: cd ..)
    ```
2.  Run the ADK Dev UI:
    ```bash
    adk web
    ```
3.  Open the URL that appears in the terminal (usually `http://localhost:8080`) in your browser.

### The Thematic Test (Halloween)

To test if your agent works as expected, use the following query in the chat interface:

> **Query:** "Analyze the historical and psychological impact of 19th-century Gothic literature."

Observe the "trace" (the thought log) on the right side. See if the agent follows your steps: if it calls the `Google Search` tool and synthesizes the response as you requested.

-----

## 5\. (Optional) Extra Challenges

If you finish early, try to:

  * Modify the instruction so the final response is formatted in a specific JSON.
  * Create a second tool (a simple Python function, e.g., `get_current_date`) and add it to the agent's `tools` list.