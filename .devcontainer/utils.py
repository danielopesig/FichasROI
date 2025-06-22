
def render_racetrack():
    # Ordem simulada estilo RaceTrack circular
    numbers = [
        0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27,
        13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33,
        1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26
    ]
    return (
        '<div style="text-align:center; font-size:20px;">' +
        " ● ".join([f"<span style='color:gold'>{n}</span>" for n in numbers]) +
        "</div>"
    )

def get_ideal_entry(last5):
    # Exemplo simples baseado em alvos comuns
    table = {
        0: [32, 26],
        5: [35, 15, 25],
        24: [35, 15, 25],
        35: [15],
        20: [6],
        2: [4, 21],
        3: [26],
    }
    count = {}
    for n in last5:
        targets = table.get(n, [])
        for t in targets:
            count[t] = count.get(t, 0) + 1
    return [k for k, v in sorted(count.items(), key=lambda item: -item[1])][:2]
