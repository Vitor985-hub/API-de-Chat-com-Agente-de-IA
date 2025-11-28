# 💬 API de Chat com Agente de IA (FastAPI + Strands Agents + Ollama)

Este projeto implementa uma API de **chat** simples que se conecta a um **Agente de IA**.  
O agente é capaz de:

- Responder perguntas gerais usando um modelo de linguagem local via **Ollama**  
- Detectar quando a pergunta envolve matemática  
- Usar uma **Tool de Cálculo** para realizar operações matemáticas

O projeto é estruturado de forma **simples, limpa e fácil de manter**, seguindo boas práticas de organização.

---

# 📌 Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI** — criação da API
- **Strands Agents SDK** — agente de IA e gestão de ferramentas
- **Ollama** — execução local do modelo LLM
- **python-dotenv** — leitura de variáveis de ambiente
- **Uvicorn** — servidor ASGI

---

# 📂 Estrutura do Projeto
````
.
├── main.py # API FastAPI
├── agent.py # Configuração do agente de IA
├── tools.py # Tool de cálculo matemático
├── config.py # Carrega variáveis do .env
├── requirements.txt # Dependências
├── .env # Configurações do modelo LLM
└── README.md.
````

---

# ⚙️ Instalação e Execução

## 1️⃣ Criar e ativar um ambiente virtual (opcional, mas recomendado)

### Windows
````
python -m venv .venv
````
Ative o ambiente
````
.venv\Scripts\activate
````

### Linux/Mac
````
python3 -m venv .venv
````
````
source .venv/bin/activate
````
---

## 2️⃣ Instalar dependências

````
pip install -r requirements.txtpip install -r requirements.txt
````

---

## 3️⃣ Instalar e configurar o Ollama

Instale o Ollama:

👉 https://ollama.com/download

Baixe o modelo (usei "llama3", mas pode ser outro):
````
ollama pull llama3
````

Inicie o servidor:
````
ollama serve
````

---

## 4️⃣ Executar a API
````
uvicorn main:app --reload
````

A API ficará disponível em:

👉 **http://localhost:8000**

---

# 🚀 Testando o Endpoint

### Rota:
````
POST /chat
````

### Corpo da requisição (JSON):
```
{
  "message": "Quanto é 1234 * 5678?"
}
```
Resposta esperada:
````
{
  "response": "7006652"
}
````
---
🧠 Funcionamento do Agente

O agente funciona assim:

Recebe a entrada enviada via /chat

Se identificar expressão matemática → usa a MathTool

Caso contrário → responde usando o modelo LLM

Retorna a resposta no formato JSON

---
🛠 Exemplos de Perguntas
Matemática:

"Quanto é 2 + 2?"

"Qual a raiz quadrada de 144?"

"1234 * 5678?"

Gerais:

"Quem foi Albert Einstein?"

"Explique o que é aprendizado de máquina."

"Qual é a capital da Itália?"

---

📝 Considerações Finais

Este projeto foi desenvolvido como um desafio técnico, com foco em:

simplicidade

clareza

organização

boas práticas

entendimento real do fluxo entre API ↔ Agente ↔ Tool

O código foi mantido o mais direto possível para facilitar manutenção e estudo.

---
👤 Autor

Vitor Eiji

GitHub:
````
https://github.com/Vitor985-hub
````
