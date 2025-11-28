from strands_agents import agent
from strands_agent.llms import ollamaLLM
from tools import MathTool
from config import ollama_model

llm = ollamaLLM(model = ollama_model)

agent = agent(
    llm = llm,
    tools = [MathTool()],
    instructions = """
você é um agente que responde perguntas.
se a pergunta envolver matematica, use math_tool.
caso o contrario, responda normalmente."""
)