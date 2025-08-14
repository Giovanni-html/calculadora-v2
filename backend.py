from math import sqrt


def calculadora(rola):
    try:
        if "%" in rola:
            partes = rola.split("%")
            return (float(partes[0]) / 100) * float(partes[1])

        elif "**" in rola:
            partes = rola.split("**")
            return float(partes[0]) ** float(partes[1])

        elif "sqrt" in rola:
            partes = rola.split("sqrt")
            antes = float(partes[0]) if partes[0] else 1
            depois = float(partes[1])
            return antes * sqrt(depois)

        else:
            return eval(rola)

    except Exception as e:
        return f"Erro: {e}"
