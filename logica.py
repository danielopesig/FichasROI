
def detectar_padroes(entrada):
    if not entrada or len(entrada) < 2:
        return "Aguardando dados suficientes"
    return "Padrão 1"

def obter_entrada_ideal(entrada):
    if not entrada:
        return []
    ultimos = entrada[:5]
    alvos = []
    for num in ultimos:
        alvos.extend([(num + i) % 37 for i in range(-1, 2)])
    contagem = {}
    for alvo in alvos:
        contagem[alvo] = contagem.get(alvo, 0) + 1
    fortes = [k for k, v in contagem.items() if v > 1]
    return fortes[:2]
