from random import randint

def generacion_id():
    id_user = randint(1,10000)
    return id_user

def alta_usuario():
    # lista para nuevo usuario
    info = []

    # ingresar datos del usuario
    print("\nEscibre los datos: ")
    id_user = generacion_id() 
    # .strip() elimina los espacios en blanco del inicio y del final
    nombre = input("Nombre: ").strip()
    ap = input("Apellido Paterno: ").strip()
    am = input("Apellido Materno: ").strip()
    fn = input("Fecha de nacimiento: ").strip()
    dir = input("Direccion: ")

    # agreagr los datos del usuario a la lista
    info.append(id_user)
    info.append(nombre)
    info.append(ap)
    info.append(am)
    info.append(fn)
    info.append(dir)

    # retornar la lista con el nuevo usuario
    return info

