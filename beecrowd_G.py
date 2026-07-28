vitimas = set()
assassinatos = {}
while True:
    try:
        assassino, vitima = input().split()
        vitimas.add(vitima)
        if assassino not in assassinatos:
            assassinatos[assassino] = 1
        else:
            assassinatos[assassino] += 1
    except EOFError:
        break
print("HALL OF MURDERERS")
for nome in sorted(assassinatos):
    if nome not in vitimas:
        print(nome, assassinatos[nome])