N = int(input())

for _ in range(N):
    M = int(input())
    fruta_preco = {}
    total = 0
    for _ in range(M):
        fruta, preco = input().split()
        fruta_preco[fruta] = float(preco)
    P = int(input())
    for _ in range(P):
        fruta, quantidade = input().split()
        preco_fruta_qtd = (fruta_preco.get(fruta)) * int(quantidade)
        total += preco_fruta_qtd
    print(f"R$ {total:.2f}")