texto = input("Escribe un texto")
texto_A = texto.split(" ")
texto_B = "".join(texto_A)
print(texto_B)
sin_vocales = []
for letra in texto_B:
    if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
        print(letra)
        sin_vocales.append(letra)      
a = ""
for i in sin_vocales:
  a += i 
print(a)