# funciones de python
from random import randint
from os import system

# funciones del sistema
from utilidades import validar_campo
from utilidades import validar_fecha

def generacion_id():
    id_user = randint(1,10000)
    return id_user

def alta_usuario():
    system("clear")
    # lista para nuevo usuario
    info = []

    # ingresar datos del usuario
    print("\nAlta usuario")
    id_user = generacion_id() 
    # .strip() elimina los espacios en blanco del inicio y del final
    # .capitalize() hace que la primera letra sea en mayuscula
    nombre = validar_campo("Nombre: ",str,"String").strip().capitalize()
    ap = validar_campo("Apellido Paterno: ",str,"String").strip().capitalize()
    am = validar_campo("Apellido Materno: ",str,"String").strip().capitalize()
    fn = validar_fecha("Fecha de nacimiento")
    dir = validar_campo("Correo electronico: ",str,"String").strip().lower()

    # agreagr los datos del usuario a la lista
    info.append(id_user)
    info.append(nombre)
    info.append(ap)
    info.append(am)
    info.append(fn)
    info.append(dir)

    # retornar la lista con el nuevo usuario
    return info

