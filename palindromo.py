print("Palíndromo checker 1.0")
frase = "Dabale arroz a la zorra el abad".lower()
frase=frase.split(" ")
print(frase)
frase_2 = "".join(frase)
print(frase_2)
frase_reversed = frase_2[::-1]
print(frase_reversed)
if (frase_2 == frase_reversed):
    print("es un palindromo")
else:
    print("no es un palindromo")