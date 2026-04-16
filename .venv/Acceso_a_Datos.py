import sqlite3 as dbapi # dbapi es una api estandar para manejo de base de datos

print(dbapi.apilevel) # para indicar la version del dbapi
print(dbapi.threadsafety)
# Sirve para indicar qué tan seguro es usar una librería de base de datos en entornos con múltiples hilos (threads).
# si sale 3 permite la ejecución de hilos totalmente segura
# 0	Nada
# 1	Solo el módulo
# 2	Módulo + conexiones
# 3	Todo
print (dbapi.paramstyle) # forma en que pasas variables a SQL de forma segura
# 🔸 Con símbolos simples
# qmark → ?
# numeric → :1
# 🔸 Con nombres
# named → :id
# pyformat → %(id)s
# 🔸 Tipo printf
# format → %s
# ejemplo
#cursor.execute("SELECT * FROM tabla WHERE id = %(id)s",{"id": 5})


# CONECTAR BBDD
# conexion con statement -> sql
#  statement  -> executeQuery  - executeUpdate
# executeQuery -> Resultset


conexion = dbapi.connect("otraBase.dat")
print(conexion)

cursor = conexion.cursor()
print(cursor)

try:
    cursor.execute("""create table if not exists usuarios( dni text, nome text, edade int)""")
except OperationalError as e:
    print(e)

''' # solo una vez ejecuto , luego coloco comillas
cursor.execute ("""drop table usuarios""")
cursor.execute ("""drop table contrasinais""")
cursor.execute ("""create table if not exists usuarios ( usuario text, contrasinal text)""")
cursor.execute ("""drop table usuarios""")
cursor.execute ("""create table if not exists contrasinais ( usuario text, contrasinal text)""")
cursor.execute ("""insert into contrasinais values('Pedro','hola')""")
conexion.commit()

'''


cursor.execute("""Select * from contrasinais""")
for rexistro in cursor.fetchall():
    # los métodos fetch* se usan para recuperar resultados de una consulta (SELECT) después de hacer cursor.execute().
    # Los datos se consumen en orden:
    # Cada fetch avanza el cursor
    # No vuelve al inicio automáticamente
    # tipos de fetch
    # fetchone()	devuelve 1 fila
    # fetchmany(n)	n filas
    # fetchall()	todas las filas
    print(rexistro)
    print(f"Usuario: {rexistro[0]}")
    print(f"Contrasinal: {rexistro[1]}")
    #print(f"Edade: {rexistro[2]}")

usu = input("Ingrese su usuario: ")
contra = input("Ingrese o contrasinal: ")

# forma mala porque concatena strings
cursor.execute("Select contrasinal from contrasinais where usuario ='" + usu + "' and contrasinal ='" + contra + "'")
# Select contrasinal from contrasinais where usuario ='Ninidea' and contrasinal ='Ninidea' or '1'='1'"     -> Ninidea' or '1'='1
print("Proba de sql injection")
for rexistro in cursor.fetchall():
    print(rexistro)

# forma de evitar el sql de injection, usa parametros para más seguridad
# ? → (sqlite)
# %s → (mysql/postgres)
# %(id)s → (pyformat)

cursor.execute("Select contrasinal from contrasinais where usuario = ? and contrasinal =?", (usu, contra))
print("Proba de sql injection con procesado")
for rexistro in cursor.fetchall():
    print(rexistro)
conexion.close()