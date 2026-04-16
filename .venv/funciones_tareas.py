# boletin 6
# EJERCICIO 3
print("-----EJERCICIO 3 -----")
# Escribir un programa que almacene nunha lista
# os números do 1 o 10 e os mostre por pantalla en orden inverso separados por comas.
numeros = list(range(1, 11))
numeros.reverse()
print(numeros)

lista = [1,2,3,4,5]
print(lista[::-1])
lista.reverse()
print(lista)
lista3 = [1,2,3,4,5,6,7,8,9,10]
for i in range (len(lista3), 0 , -1): # len es la longitud de lista 3
    print(lista3[i-1])

 # a parecer es más rapido el print, pero en realidad es más largo y con programas grandes
 # se hace mejor con el for.
print("-----EJERCICIO 5 -----")
#Escribir un programa que almacene o abecedario nunha lista,
#e cree outra lista a partir dela, onde non aparezan as letras que ocupen posicións múltiplos de 3,
#e mostre por pantalla a lista resultante.
abecedario = "abcdefghijklmnopqrstvwxyz"
listaAux = []
for i, letra in enumerate(abecedario): # enumerate recorre un numero por cada elemento
    if not i%3 == 0:
        listaAux.append(letra)
print(listaAux)

print (abecedario [3:10]) # slice para seleccionar tajadas de la lista, tuplas, string que yo quiera
print (abecedario [20:-3])
print(abecedario [:]) # se sobre entiende que es desde 0 hasta el final
print(abecedario [::3]) # desde el principio al final pero va de 3 en 3
print(abecedario[::-1])