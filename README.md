# 💬 API de Chat com Agente de IA 

Esta aplicação implementa uma API FastAPI que expõe um endpoint de chat integrado a um agente Strands, utilizando um modelo rodando no Ollama com suporte a tools (funções externas).
Permite enviar mensagens para o agente e receber respostas estruturadas.
---

# 📦 Tecnologias utilizadas

FastAPI — Framework para construção de APIs rápidas em Python

Strands Agents — Framework para criação de agentes com ferramentas

Ollama — Execução local de modelos LLM

Uvicorn — Servidor ASGI

Python 3.11+

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
⚙️ Pré-requisitos

Antes de executar a API, instale:

✔️ Python 3.11+
✔️ Ollama instalado

Baixe em: https://ollama.com/download

✔️ Baixe um modelo compatível com tools

Recomendado:
````
ollama pull llama3.1
````

Ou outro modelo que você definir no .env.

---
# ⚙️ Instalação e Execução

📦 Instalação
1️⃣ Crie o ambiente virtual
python -m venv .venv

2️⃣ Ative o ambiente

Windows:
````
.venv\Scripts\activate
````
3️⃣ Instale as dependências
````
pip install -r requirements.txt
````
▶️ Executando a API

Com tudo configurado, rode:
````
uvicorn main:app --reload
````

A API estará disponível em:

📍 http://127.0.0.1:8000

Documentação interativa:

📄 http://127.0.0.1:8000/docs


---

# 🚀 Testando o Endpoint

Exemplo usando curl:
````
curl -X POST "http://127.0.0.1:8000/chat" \
-H "Content-Type: application/json" \
-d "{\"Message\": \"Olá, quem é você?\"}"
````
Resposta esperada:
````
{
  "response": {
    "message": {
      "role": "assistant",
      "content": [
        { "text": "Olá! Eu sou seu agente de IA..." }
      ]
    }
  }
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
