from strands import Agent
from strands.models.ollama import OllamaModel
from tools import math_tool

ollama_model = OllamaModel(
    host='http://localhost:11434',
    model_id='llama3.1'
)

chat_agent = Agent(
    model = ollama_model,
    tools = [math_tool],
    system_prompt= "Você só deve usar a math_tool quando o usuário pedir explicitamente "
    "um cálculo matemático ou enviar uma expressão matemática. "
    "Para saudações e conversas normais, responda normalmente."
)