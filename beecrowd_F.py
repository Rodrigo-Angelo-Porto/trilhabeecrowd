while True:
    lista_intervalos = []
    try: 
        linha = input().strip() 
        if linha == "": 
            continue
        N = int(linha)
        for _ in range(N):
            X, Y = map(int, input().split())
            for valor in range(X, Y+1):
                lista_intervalos.append(valor)
        lista_intervalos_ordenada = sorted(lista_intervalos)
        Num = int(input())
        primeira_posicao = None
        ultima_posicao = None
        for posicao, valor in enumerate(lista_intervalos_ordenada):
            if valor == Num:
                if primeira_posicao is None:
                    primeira_posicao = posicao
                ultima_posicao = posicao
        if primeira_posicao is None:
            print(f"{Num} not found")
        else:
            print(f"{Num} found from {primeira_posicao} to {ultima_posicao}")
    except EOFError:
        break
    