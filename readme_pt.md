# 🏛️ Workshop: Engenharia de Agentes Autónomos com Google ADK

Bem-vindo ao workshop sobre o Agent Development Kit (ADK) da Google.

Nesta sessão, vamos ultrapassar a teoria dos LLMs e mergulhar na prática da engenharia de agentes. O nosso objetivo é focar-nos na "lógica" de um agente, completando um esqueleto de código para construir um **"ScholarAgent"** – um agente de IA autónomo capaz de pesquisar fontes académicas na web e sintetizar uma resposta.

Este repositório contém todo o material de que precisas:

  * `requirements.txt`: As dependências Python.
  * `adk_scholar_workshop/agent.py`: O esqueleto do nosso agente, que iremos editar.

## 1\. Passos de Setup (Obrigatório)

Para garantir que os 90 minutos são focados em desenvolvimento, é **essencial** que chegues à sessão com o seguinte setup concluído.

### a. Instalar Python

Certifique-se de que tem o **Python 3.9 ou superior** instalado e a funcionar no terminal.  
Sugestão: Para gerir melhor os ambientes, recomendamos vivamente o uso de [UV](https://github.com/astral-sh/uv) da Astral. As instruções seguintes assumem que está a utilizá‑lo.

### b. Obter API Keys (O Passo Mais Importante)

Um agente é composto por um "cérebro" (LLM) e "mãos" (Ferramentas). Ambos requerem APIs.

**i. Chave da API Gemini (O "Cérebro"):**

1.  Visita o [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  Faz login e clica em "Create API key".
3.  **Copia e guarda esta chave.**

**ii. Chaves da API Google Search (As "Mãos"):**
Este passo tem 2 partes e é o mais complexo:

  * **Custom Search Engine ID:**
    1.  Vai ao [Programmable Search Engine](https://programmablesearchengine.google.com/) e clica em "Adicionar".
    2.  Configura-o para "Pesquisar em toda a Web". Dá-lhe um nome (ex: "ADK Search").
    3.  Após criar, clica em "Editar motor de pesquisa" -\> "Informações básicas" e copia o **ID do motor de pesquisa (CSE ID)**.
  * **API Key:**
    1.  Vai à [Google Cloud Console](https://console.cloud.google.com/apis/library/customsearch.googleapis.com).
    2.  Ativa a **"Custom Search API"** para um projeto teu.
    3.  Vai a "Credenciais", clica em "Criar Credenciais" -\> "Chave de API".
    4.  **Copia e guarda esta chave.**

-----

## 2\. Inicialização do Projeto (Hands-On)

Iremos começar o workshop prático aqui.

### a. Clonar o Repositório (Se ainda não o fizeste)

```bash
# Faz o clone do repositório
git clone https://github.com/duarte-cruz/adk_workshop.git
cd adk_workshop
```

### b. Instalar Dependências

1.  Crie o seu ambiente virtual com o `uv`:

    ```bash
    uv venv
    ```

2.  Active o ambiente:

    * **Linux/macOS (bash/zsh):**
      ```bash
      source .venv/bin/activate
      ```
    * **Windows (Command Prompt / Git Bash):**
      ```bash
      .venv\Scripts\activate
      ```
    * **Windows (PowerShell):**
      ```powershell
      .venv\Scripts\Activate.ps1
      ```

3.  Instale as dependências a partir do ficheiro  usando o `uv`:

    ```bash
    uv pip install -r requirements.txt
    ```

### c. Criar Ficheiro de Ambiente (.env)

1.  Navega para a pasta do agente:

    ```bash
    cd adk_scholar_workshop
    ```

2.  Dentro de `adk_scholar_workshop`, cria um ficheiro chamado `.env`.

3.  Cola o seguinte conteúdo, substituindo `[...]` pelas chaves que obtiveste na Parte 1:

    ```ini
    # Ficheiro: adk_scholar_workshop/.env

    # Chave do Google AI Studio
    GEMINI_API_KEY=[A_TUA_CHAVE_GEMINI_API_KEY]

    # Chaves da Google Search API
    GOOGLE_API_KEY=[A_TUA_CHAVE_DA_GOOGLE_CLOUD_API]
    GOOGLE_CSE_ID=[O_TEU_ID_DE_MOTOR_DE_PESQUISA_CSE_ID]
    ```

-----

## 3\. A Tarefa: Completar o "ScholarAgent"

O teu objetivo é abrir o ficheiro `adk_scholar_workshop/agent.py` e completar as secções marcadas com `TODO`.

Este é o esqueleto que irás encontrar:

```python
# adk_scholar_workshop/agent.py
# ... (importações e verificações)
    
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

### TODO 1: A Instrução (AGENT\_INSTRUCTION)

Substitui o texto `"TODO: ..."` dentro da variável `AGENT_INSTRUCTION` por uma instrução de nível académico detalhada.

**Requisitos para a Instrução:** O agente deve ser instruído a:

  * Identificar-se como "ScholarAgent", um assistente de investigação.
  * Receber um tópico complexo do utilizador.
  * Usar *explicitamente* a ferramenta `Google Search` (o ADK sabe que este é o nome da ferramenta `Google Search`).
  * Encontrar um mínimo de 3 fontes de alta qualidade (académicas, artigos, etc.).
  * Extrair o argumento principal de cada fonte.
  * Sintetizar todos os argumentos numa resposta final coesa, citando as fontes (Título e URL).

### TODO 2: Adicionar a Ferramenta

Na definição do `root_agent`, falta o parâmetro `tools`. Adiciona o parâmetro `tools` e passa-lhe a ferramenta `Google Search` (que já foi importada).

**Dica:** A definição final do agente deve ficar parecida com:

```python
root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='ScholarAgent', # <-- Boa ideia mudar o nome
    description='Um agente de investigação que pesquisa e sintetiza fontes.', # <-- E a descrição
    instruction=AGENT_INSTRUCTION,
    tools=[google_search] # <-- A tua solução para o TODO 2
)
```

-----

## 4\. Executar e Testar

Quando te sentires confiante com as tuas alterações ao `agent.py`, guarda o ficheiro.

1.  Certifica-te no terminal estás dentro da raiz da aplicação ``:
    ```bash
    # (Se estiveres na pasta adk_scholar_workshop executa: cd ..)
    ```
2.  Executa o ADK Dev UI:
    ```bash
    adk web
    ```
3.  Abre o URL que aparece no terminal (normalmente `http://localhost:8080`) no teu browser.

### O Teste Temático (Halloween)

Para testar se o teu agente funciona como esperado, usa o seguinte *query* na interface de chat:

> **Query:** "Analisar o impacto histórico e psicológico da literatura gótica do século XIX."

Observa o *trace* (o registo de pensamentos) no lado direito. Vê se o agente segue os teus passos: se chama a ferramenta `Google Search` e se sintetiza a resposta como lhe pediste.

-----

## 5\. (Opcional) Desafios Extra

Se terminares mais cedo, tenta:

  * Modificar a instrução para que a resposta final seja formatada num JSON específico.
  * Criar uma segunda ferramenta (uma simples função Python, ex: `get_current_date`) e adicioná-la à lista de `tools` do agente.