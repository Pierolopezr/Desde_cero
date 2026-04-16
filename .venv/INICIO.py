#Tipado estatico
 # int numero = 2.(un numero cualquiera);
#tipado dinamico
numero = "Maria"
print(type(numero))
numero = 2
print(type(numero))
print(isinstance(numero, int))
def sumar (a, b):
    return a + b
print(sumar("hola ", "que tal"))

#CADENAS
#tipo string
cadena = 'Pueden ser con comilla "doble" o simple'
cadena2 = "Puede ir con comilla 'simple'"
#comentario de una linea
"""Comentarios multilinea
    Estos suelen usars para hacer javadocs
"""

print(cadena)
print(cadena2)
#tipo coma flotante
num2= 2.6
num3= 0.4e-6
print(type(num3))
#tipo booleano
booleano = True
print(type(booleano))
#tipo completo
complejo = 4 + 4.5j
print(type(complejo))

#Operadores aritmeticos
# + - * /
# ** potencia
# % resto
# // division entera  -> 1.5 // 1 = 1

# Operaciones a nivel de bit
# & | ^ ~ << >>
print (2&3)  # me lo devuelve en decimal
print (0b11110011 & 0b01110001)

#Operaciones de cadena
# + *
print ("Hola " * 2)

#Operadores booleanos
# Java &&  ||  !
# Python and or not
# == != <= >= < >

cadea = "uno"
# valor = (cadea.equals("Uno")?1:0;
valor = 1 if cadea == "uno" else 0
print(valor)



#----------------------#

# --- Bucles y Condicionales ---
from unittest import case

import random
def gen_num():
    numero = random.randint(0, 10)
    return numero

def gen_hora():
    hora = random.randint(00, 23)
    return hora

def gen_seg():
    seg = random.randint(00, 59)
    return seg

n = gen_num()
if n > 5:
    print(f"el número {n} es mayor que 5")
elif n == 5:
    print("El número es igual a 5")
elif n < 0:
    print(f"El número {n} es negativo")
else:
    print(f"El número {n} es menor que 5")


opcion = gen_num()
if opcion == 1:
    print("Opción 1")
elif opcion == 2:
    print("Opcion 2")
elif opcion == 3:
    print("Opcion 3")

match opcion:  # Es el switch-case de java
    case 1:
        print("Opcion 1")
    case 2:
        print("Opcion 2")
    case 3:
        print("Opcion 3")
    case 4|5|6:
        print("Opcion 4, 5 y 6")
    case _:
        print("Las opciones válidas son del 1 al 6")


l = [gen_num(), gen_num(), gen_num(), gen_num(), gen_num()]
match l:
    # PARA LOS CASE SE TOMA EL QUE SE PAREZCA IGUAL A LA TABLA L
    case [x, y]:
        print(f"Dos elementos en la lista: {x} y {y}")
    case [me, cago, en, la, puta]:
        print(f"El elemento {me} es {cago}")


persona = {"nombre": "Hatsune Miku", "numero": 1}
match persona:
    case {"nombre": nombre, "numero": numero}:
        print(f"La reina del mundo es: {nombre}. La número  {numero}")
    case {"nombre": nombre}:
        print(f"¿Quién? {nombre}")


class Figura:
    pass

class circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

fig = circulo(gen_num())
match fig:
    case circulo(radio=0):
        print("No existe un circulo con radio 0")
    case circulo(radio=r):
        print(f"El circulo con radio: {r}")
    case Rectangulo(base=b, altura=a):
        print(f"El rectangulo con base: {b}x{a}")
    case _:
        print("Figura desconocida")


horas = [gen_hora(), gen_seg()]
match horas:
    case [e, i]:
        print(f"Son las {e}:{i}")


print("-------BUCLES------")
print("----FOR-----")
# Bucles
# Bucles definidos FOR
for n in l: print(n) # l su contenido está más arriba
    # for(m=5; m<10; m++): print(m) su equivalente es en python
    # for in rage(0.5.1):print(n)  -> el 1 indica como un n+1

print("-----WHILE----")
# Bucles indefinidos  WHILE

n= 0
while n < 5:
    print(n);
    n+=1

print("---------COLECCIONES----------")
#### Colecciones
# lista: Sirven para almacenar secuencias de elementos. Es una colección de objetos arbitrarios.
# Tuplas: Tienen como utilidad representar datos inmutables, como coordenadas o constantes.
# diccionario: Para almacebar datos asociados, donde para el acceso al valor será util una clave
#Conjuntos: Para almacenar elementos únicos, realizar operaciones de conjuntos y eliminar duplicados.

# Características
# Orden: Las listas y tuplas mantienen un orden definido, mientras que los diccionarios y conjuntos no.
# Mutabilidad: Las listas y diccionarios son MUTABLES( pueden modificarse despues de su creacion),
    # mientras que las tuplas y conjuntos (set) NO SON MUTABLES.
#dinamicas: (pueden aumentar de numero)
#Indices absolutos(desde 0 pa delante) o relativos (desde 0 para atras)


# Listas (caracterizan los [])
print("-----LISTAS------")
lista = [1,2,3,4,5.0,"Seis", [7,8,9,["Diez","Once"]]]
lista[2]= "Tres"
print(lista)
print(type(lista))
lista.append(6)  # AÑADE otro elemento
print(lista)
print(lista.pop(3)) # BORRA Y TE MUESTRA EL ELEMENTO BORRADO


print("-----TUPLAS------")
# Tuplas (Lo caracterizan las ',' comas, parentessis NO)
tupla = (1,2,3,4,5.0,"Seis", [7,8,9,("Diez","Once")])  # me puedo cargar el obejto dupla "dez, once" a libertad
                                                       # osea puedo convertirlo a lista, ya que esta dentro de una lista
                                                       # pero NO puedo cambiar el objeto lista que lo engloba-
tupla2 = 2,4,5
print(type(tupla2));
print(type(tupla));
tupla [6][0] = "Siete"  # el 0 indica la posicion dentro de otra posicion
print(tupla)

# Diccionario
print("----DICCIONARIO----") # CLAVE : VALOR
d= {1: "Un", 2:"Dos",3: "tres ", "Azul" :"#0000ff"}
print(d[1])
print(d)
print(type(d))
print(d['Azul'])
d["Tres"]=3.0

# Conjuntos
print("----CONJUNTOS----") # Los repetidos se van a tomar po culo
s ={1,2,3,4,4,4}
s2 = set([3,4,5,6,6,6])
s.add(5)  # añade un valor
s2.update((6,7,8)) # añade más valores
s.remove(2) # elimina pero puede haber errores si no existe
s2.discard(3)  # elimina pero no nos da error en caso que no exista
print(s, s2)
print(s.union(s2))
print(s.intersection(s2))
print(s.difference(s2))
print(s.symmetric_difference(s2))


# PROGRAMACIÓN ORIENTADA A OBJETOS
 