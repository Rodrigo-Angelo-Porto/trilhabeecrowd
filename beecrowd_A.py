N = int(input())

prioridades = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3,
    }

for _ in range(N):
    resposta = ""
    pilha = []

    expressao = input().strip()

    for i in expressao:
        if i.isalnum():
            resposta += i

        elif i == "(":
            pilha.append(i)

        elif i == ")":
            while pilha[-1] != "(":
                resposta += pilha.pop()

            pilha.pop()

        elif i in prioridades:
            while (
                pilha
                and pilha[-1] != "("
                and prioridades[pilha[-1]] >= prioridades[i]
            ):
                resposta += pilha.pop()

            pilha.append(i)
            
    while pilha:
        resposta += pilha.pop()

    print(resposta)