# API-de-Chat-com-Agente-de-IA
...existing code...
# API de Chat com Agente de IA

Pequeno projeto que expõe um endpoint FastAPI para um agente conversacional que pode usar ferramentas (por exemplo cálculo simples).

Principais arquivos
- [README.md](README.md)
- [.env](.env)
- [.gitignore](.gitignore)
- [config.py](config.py) — contém a variável [`ollama_model`](config.py)
- [tools.py](tools.py) — implementa a ferramenta de cálculo [`MathTool`](tools.py)
- [agent.py](agent.py) — instancia o agente e a variável exportada [`agent`](agent.py)
- [main.py](main.py) — servidor FastAPI e modelo pydantic [`Message`](main.py)
- [requiriments.txt](requiriments.txt)

Requisitos
- Python 3.8+
- Instalar dependências:
```sh
pip install -r requiriments.txt

Configuração

Ajuste o modelo em .env ou em config.py:
Ex.: ollama_model = llama3

como rodar

uvicorn main:app --reload

Endpoint

POST /chat
Body JSON esperado: {"Message": "texto"} (observe a chave Message em maiúscula — Message)
Resposta: {"response": "<texto do agente>"}
Exemplo curl

curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d '{"Message":"2+2"}'