def verificar_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]
    
texto = "Socorram-me, subi no ônibus em Marrocos"
if verificar_palindromo(texto):
    print(texto, "é um palíndromo.")
else:
