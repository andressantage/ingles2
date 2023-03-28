palabra = input("Ingrese la palabra: ")
letras = list(palabra)
print(letras)
vocales = 'aeiou'
consonantes = 'bcdfghjklmnñpqrstvwxyz'

for i in range(len(letras)):
    if letras[i-2] in consonantes and letras[i-1] in vocales and letras[i] in consonantes:
        letras.insert(i-2,'-')

#for i in range(len(letras)):
    #if letras[i] in vocales and letras[i+1] in consonantes and letras[i+2] and letras[i+3] in vocales:
    #    letras.insert(i+2,'-')
    #    letras.insert(i+5,'-')
    #if letras[i] in vocales and letras [i+i] in consonantes:
    #    letras.insert(i+1, '-')
    #if letras [i] == 'b' and letras[i+1] == 'r':
    #    letras.insert(i+3,'-')

#if letras[len(letras) - 1] == '-':
#    letras.pop((len(letras) - 1))
print(letras)