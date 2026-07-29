set_palavras=set()
while True:
    try:
        frase=input()
        frase_limpa=""
        for caractere in frase:
            caractere=caractere.lower()
            if "a" <= caractere <= "z":
                frase_limpa += caractere
            else:
                frase_limpa += " "
        for palavra in frase_limpa.split():
            set_palavras.add(palavra)
    except EOFError:
        break
for palavra in sorted(set_palavras):
    print(palavra)