while True:
    try:
        contador = 0
        N = int(input())
        lista_numeros = []
        for i in range(N):
            Xi = input()
            lista_numeros.append(Xi)
        lista_numeros.sort()
        for i in range(1, N):
            atual = lista_numeros[i]
            anterior = lista_numeros[i - 1]
            for j in range(len(atual)):
                if atual[j] == anterior[j]:
                    contador += 1
                else:
                    break
        print(contador)
    except EOFError:
        break