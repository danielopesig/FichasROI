def detectar_padroes(historico):
    if len(historico) < 5:
        return [], "Aguardando dados suficientes", []
    ultimos = historico[-5:]
    alvos = []
    for n in ultimos:
        vizinhos = [(n + i) % 37 for i in range(-1, 2)]
        alvos.extend(vizinhos)
    contagem = {x: alvos.count(x) for x in set(alvos)}
    entrada_ideal = [n for n, v in contagem.items() if v > 1]
    padrao = "🎯 Padrão de precisão identificado – Entrada ideal com 3 fichas" if entrada_ideal else "⚠️ Nenhum padrão forte detectado"
    return entrada_ideal, padrao, entrada_ideal