# 🏛️ Workshop: Engenharia de Agentes Autónomos com Google ADK

Bem-vindo ao workshop de 90 minutos sobre o Agent Development Kit (ADK) da Google.

Nesta sessão, vamos ultrapassar a teoria dos LLMs e mergulhar na prática da engenharia de agentes. O nosso objetivo é construir, instrumentar e testar um **"ScholarAgent"** – um agente de IA autónomo capaz de receber um tópico de investigação, pesquisar fontes académicas na web e sintetizar uma resposta coesa.

## 1\. Passos de Setup (Obrigatório)

Para garantir que os 90 minutos são focados em desenvolvimento, é **essencial** que chegues à sessão com o seguinte setup concluído.

### a. Instalar Python

Certifica-te que tens o **Python 3.9 ou superior** instalado e a funcionar no teu terminal.
*Sugestão: Para poderes fazer uma melhor gestão de ambientes, recomendamos que utilizes uma ferramenta como o [Conda](https://docs.conda.io/en/latest/miniconda.html) ou [UV](https://github.com/astral-sh/uv).*

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

Iremos começar o workshop prático aqui. Vamos criar uma pasta raiz para o nosso workshop, instalar as ferramentas (incluindo o `adk`) e, de seguida, usar o `adk` para criar o projeto do nosso agente.

### a. Criar Diretoria Raiz e Instalar Dependências

1.  Cria a diretoria principal do workshop e entra nela:

    ```bash
    mkdir WorkshopADK
    cd WorkshopADK
    ```

2.  Cria um ficheiro chamado `requirements.txt` nesta pasta (`WorkshopADK/requirements.txt`).

3.  Cola as seguintes dependências nesse ficheiro:

    ```txt
    # Ficheiro: requirements.txt
    google-adk
    google-api-python-client
    google-auth-oauthlib
    python-dotenv
    ```

4.  Instala estas dependências (idealmente dentro do teu ambiente virtual Conda/UV):

    ```bash
    pip install -r requirements.txt
    ```

    (Agora já tens o comando `adk` disponível no teu terminal.)

### b. Criar a Estrutura do Agente

1.  Ainda dentro da pasta `WorkshopADK`, executa o comando `adk create` para criar a subpasta do nosso agente:
    ```bash
    adk create adk_scholar_workshop
    ```
2.  Caso seja necessário escolher o modelo, seleciona a opção **"Other models (fill later)"**.
3.  Agora terás a seguinte estrutura de pastas:
    ```
    WorkshopADK/
    ├── requirements.txt
    └── adk_scholar_workshop/
        ├── agent.py
        └── ... (outros ficheiros do ADK)
    ```

### c. Criar Ficheiro de Ambiente (.env)

1.  Entra na pasta do agente que acabaste de criar:

    ```bash
    cd adk_scholar_workshop
    ```

2.  Dentro de `adk_scholar_workshop`, cria um ficheiro chamado `.env`.

3.  Cola o seguinte conteúdo, substituindo `[...]` pelas chaves que obtiveste na Parte 1:

    ```ini
    # Ficheiro: WorkshopADK/adk_scholar_workshop/.env

    # Chave do Google AI Studio
    GEMINI_API_KEY=[A_TUA_CHAVE_GEMINI_API_KEY]

    # Chaves da Google Search API
    GOOGLE_API_KEY=[A_TUA_CHAVE_DA_GOOGLE_CLOUD_API]
    GOOGLE_CSE_ID=[O_TEU_ID_DE_MOTOR_DE_PESQUISA_CSE_ID]
    ```

-----

## 3\. A Tarefa: Dar Vida ao "ScholarAgent"

O comando `adk create` gerou o ficheiro `adk_scholar_workshop/agent.py`. Este é o esqueleto do nosso agente. Vamos modificá-lo.

Abre o ficheiro `adk_scholar_workshop/agent.py` no teu editor de código.

### O Desafio

A tua tarefa é editar o `agent.py` para cumprir os seguintes objetivos:

**1. A Instrução (O "Cérebro"):**
O ficheiro `agent.py` padrão vem com um `root_agent` que tem uma instrução genérica (`instruction='Answer user questions..._`). A tua tarefa é criar uma **instrução de nível académico** muito mais detalhada.

  * Cria uma variável (ex: `INSTRUCAO_AGENTE`) que contenha esta instrução.
  * **Requisitos para a Instrução:** O agente deve ser instruído a:
      * Identificar-se como "ScholarAgent", um assistente de investigação.
      * Receber um tópico complexo do utilizador.
      * Usar *explicitamente* a ferramenta `Google Search`.
      * Encontrar um mínimo de 3 fontes de alta qualidade (académicas, artigos, etc.).
      * Extrair o argumento principal de cada fonte.
      * Sintetizar todos os argumentos numa resposta final coesa, citando as fontes (Título e URL).

**2. A Montagem (O "Corpo"):**
Agora, modifica a definição do `root_agent` existente para usar a tua nova instrução.

  * Adiciona as importações necessárias no topo (ex: `load_dotenv` e `Google Search`).
  * Altera o `model` para o que desejas usar (ex: `'gemini-2.5-flash-lite'`).
  * Altera o `name` para algo como "ScholarAgent".
  * Altera a `description` para algo mais específico.
  * Passa a tua variável `INSTRUCAO_AGENTE` para o parâmetro `instruction`.
  * Verifica se a ferramenta `Google Search` é passada na lista `tools=[]`.

-----

## 4\. Executar e Testar

Quando te sentires confiante com o teu `agent.py`, guarda o ficheiro.

1.  Certifica-te de que estás no terminal dentro da pasta `adk_scholar_workshop`:
    ```bash
    # Se ainda estiveres em WorkshopADK, executa:
    cd adk_scholar_workshop
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