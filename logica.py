def detectar_padroes(ultimos):
    if not ultimos or len(ultimos) < 5:
        return None, []

    # Exemplo simples: repetições e somas de alvos
    contagem = {}
    for n in ultimos:
        vizinhos = [(n + i) % 37 for i in range(-1, 2)]
        for v in vizinhos:
            contagem[v] = contagem.get(v, 0) + 1

    alvos_fortes = [k for k, v in contagem.items() if v >= 2]
    padrao = "🔥 Forte" if alvos_fortes else "🧊 Fraco"
    return padrao, alvos_fortes[:2]