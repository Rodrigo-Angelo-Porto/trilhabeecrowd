morse_para_letra={
    ".-":"a",
    "-...":"b",
    "-.-.":"c",
    "-..":"d",
    ".":"e",
    "..-.":"f",
    "--.":"g",
    "....":"h",
    "..":"i",
    ".---":"j",
    "-.-":"k",
    ".-..":"l",
    "--":"m",
    "-.":"n",
    "---":"o",
    ".--.":"p",
    "--.-":"q",
    ".-.":"r",
    "...":"s",
    "-":"t",
    "..-":"u",
    "...-":"v",
    ".--":"w",
    "-..-":"x",
    "-.--":"y",
    "--..":"z"
}
t=int(input())
for _ in range(t):
    resposta=""
    linha=input()
    palavras=linha.split(".......")
    for palavra in palavras:
        letras=palavra.split("...")
        for letra in letras:
            morse=""
            simbolos=letra.split(".")
            for simbolo in simbolos:
                if simbolo=="=":
                    morse+="."
                elif simbolo=="===":
                    morse+="-"
            letra_traduzida=morse_para_letra[morse]
            resposta+=letra_traduzida
        resposta+=" "
    print(resposta.strip())