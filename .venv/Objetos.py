# Programación orientada a objetos
class Persoa(object): #


   contador = 0
   def __init__ (self, nome=None, dni=None, edade=None, **otros):  #__init__  tiene la funcion de iniciar las propiedades nome dni y edade
       # ** otros  = recoge todos los argumentos adicionales con nombre (clave=valor) en forma de diccionario
       self.nome = nome
       self.dni = dni
       self.edade = edade
       Persoa.contador += 1
       # self es para python y this es para java
       super().__init__(**otros)


   def __str__(self): # lp convierte en string
       return f"Nome: {self.nome}. DNI: {str(self.dni)}. Edade: {str(self.edade)}"
       # otra forma
       # return "Nome: " + self.nome + " DNI: " + self.dni + "Edade: " + self.edade


# p1 y p2 son instancias
p1 = Persoa(nome="Pedro", dni="12345", edade=18)
print(p1)
p2 = Persoa(nome="Juan", dni="54321", edade=19)
print(p2.nome)




class Animal(object):
   def __init__(self, nome, edade):
       self.nome = nome
       self.edade = edade


   def __str__(self):  # lp convierte en string
       return f"Nome: {self.nome}. Edade: {str(self.edade)}"


d2 = Animal("Perro", 15 )
print(d2)


class CaracteristicasMedicas():
    def __init__(self, ritmoCardiaco=None, **otros):

        self.ritmoCardiaco = ritmoCardiaco
        super().__init__(**otros)

    def __str__(self):
        return f"Ritmo Cardiaco: {self.ritmoCardiaco}"



class Deportista(Persoa, CaracteristicasMedicas  ):  # la clase usará los recursos de Persoa
   def __init__(self,nome, dni, edade, ritmo_Cardiaco ,deporte):
       super().__init__(nome=nome, dni=dni, edade=edade, ritmoCardiaco = ritmo_Cardiaco) # el super llama al init de Persoa
       self.deporte = deporte


   def __str__(self):
       return super().__str__() + f" Ritmo cardiaco: {self.ritmoCardiaco}  Deporte: {self.deporte}" # el super llama al str de la clase Persoa declarada en la clase deportista
       #return f"Nome: {self.nome}. Deporte: {self.deporte}" # es más simple que la anterior ya que usa los recursos de Persoa
d1 = Deportista("Pedro", "12345", 18,89,"Futbol")
print(d1)

class Posto:
    def __init__(self, tarefa:str, horario:int, remuneracion:float, formacion:str):
        self.tarefa = tarefa
        self.horario = horario
        self.remuneracion = remuneracion
        self.formacion = formacion

    def getTarefa(self): # obtienes
        return self.__tarefa

    def setTarefa(self, tarefa): # establece
        if isinstance(tarefa, str):
            if tarefa == "Barrer" or tarefa == "Lavar platos":
                self.__tarefa = tarefa # el __ lo oculta
            else:
                raise (TarefaNonPermitidaError(tarefa))
        else:
            raise (TypeError("Tipo de datos inadecuado para la tarefa"))

    tarefa = property(getTarefa, setTarefa)

    @property  # equivalente  lo de arriba
    def getHorario(self):
        return self.__horario

    @getHorario.setter

    def setHorario(self, horario):
        if isinstance(horario, float):
            self.__horario = horario
        else:
            raise (TypeError("Tipo de datos inadecuado para horario"))

# EXCEPCIONES

class TarefaNonPermitidaError(Exception):
    def __init__(self, tarefa):
        self.tarefa = tarefa
    def __str__(self):
        return f"Error, tarefa non permitida:  {(self.tarefa)}"

posto = Posto ("Lavar platos", 12, 4, "Peón")
posto.setTarefa("Lavar platos")
posto.tarefa="Lavar platos"
print(posto.tarefa)
print(posto.getTarefa())

posto.horario=3.5
print(posto.horario)

