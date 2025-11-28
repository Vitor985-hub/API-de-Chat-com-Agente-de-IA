from strands.tools import tool 

@tool
def math_tool(expression: str) -> str:
    """
    resolve uma expressão matematica enviada como texto.
    exemplo "2 + 2 = 4"
    """
    try:
        retult = eval(expression)
        return str(retult)
    except Exception as e:
        return f"Erro ao calcular {e}"
 