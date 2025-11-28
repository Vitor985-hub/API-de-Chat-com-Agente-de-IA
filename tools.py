from strands_agent.tools import tool

class MathTool(tool):
    name = 'math_tool'
    description = 'executa operações matematicas simples'

    def run(self, query: str) -> str:
    try:
        result = eval(query)
        return str(result)
    except Exception:
        return 'não consegui calcular isso'
