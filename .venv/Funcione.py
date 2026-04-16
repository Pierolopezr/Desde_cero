# declarar funcion
def funcion (parametro1, parametro2):
    print(parametro1)
    print(parametro2)
    return parametro1 + parametro2

res1 = funcion("Hola ", "y adios")
res2 = funcion(1,2)
print(res1)
print(res2)

# def funcion2 (parametro1, parametro2):
#     if isinstance(parametro1) == float:
#         print(parametro1)
#     else:
#         raise TypeError("El parametro1 no es float")
#         # raise significa que lanza una excepcion
#     if isinstance(parametro2) == float:
#         print(parametro2)
#     else:
#         raise TypeError("El parametro2 no es float")
#     return parametro1 + parametro2
# print(funcion2(2,2))

def funcion3 (x, y, z= 0):  # pass  significa que no va a romper nada
    print(x, y, z)

res1 = funcion("Hola ", "y adios")
res2 = funcion(1,2)
print(res1)
print(res2)

funcion3(1, 2)

def funcion5 (x, y, **koutros1):
    print(x)
    print(y)
    for clave in koutros1.keys():
        print("Clave: ", clave)
        print(koutros1[clave])
    return x, y, koutros1['z']

#investigar programacion orientada a objetos

