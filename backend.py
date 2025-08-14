from math import sqrt


def calculadora(bola):
    try:
        if "%" in bola:
            partes = bola.split("%")
            return (float(partes[0]) / 100) * float(partes[1])

        elif "**" in bola:
            partes = bola.split("**")
            return float(partes[0]) ** float(partes[1])

        elif "sqrt" in bola:
            partes = bola.split("sqrt")
            antes = float(partes[0]) if partes[0] else 1
            depois = float(partes[1])
            return antes * sqrt(depois)

        else:
            return eval(rola)

    except Exception as e:
        return f"Erro: {e}"

