# funcion para buscar el nombre del usuario
def buscar_nombre(nombre_user,lista_usuarios):
    encontrado = False
    
    # se pasan todos los atributos del usuario aunque solo se use el nombre
    for id_bd,nombre,ap,am,fn,dir in lista_usuarios:
        if (nombre == nombre_user):
            encontrado = True
            break
    
    if not encontrado:
        print("Usuario no encontrado")
    
    return encontrado

# funcion para mostar los usuarios con el nombre a buscar
def mostrar_usuarios(lista_usuarios):
    total = len(lista_usuarios)
    # nombre a buscar
    nombre = input("Nombre: ")
    nombre_encontrado = buscar_nombre(nombre,lista_usuarios)

    


