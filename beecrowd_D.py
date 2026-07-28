N = int(input())

for caso in range(N):
    M, C = map(int, input().split())
    tabela = [[] for _ in range(M)]
    numeros = [int(x) for x in input().split()]
    for i in numeros:
        posicao = i % M
        tabela[posicao].append(i)
    for indice, lista in enumerate(tabela):
        linha = f"{indice} ->"
        for numero in lista:
            linha += f" {numero} ->"
        linha += " \\"
        print(linha)
    if caso < N - 1:
        print()