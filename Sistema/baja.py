from utilidades import mostrar_usuarios
from os import system

def elminar_usuario(id_user, lista):
    for i in range(len(lista)):
        if(lista[i][0] == id_user):
            usuario_eliminado = lista.pop(i)
            print("Usuario eliminado")
            return True
        else:
            continue 

    system("pause")
    print("Presione Enter para continuar...")
    system("clear")

def baja_usuario(lista):
    system('clear')
    # consultar los usuarios con el mismo nombre
    nombre_buscar = input("Nombre a buscar: ")
    encontrado = mostrar_usuarios(lista, nombre_buscar)

    if (encontrado):
        try:
            id_usuario = int(input("ID a eliminar: "))
            elminar_usuario(id_usuario,lista)
        except ValueError:
            print("Error: el ID debe ser un numero entero")
    system("pause")
    print("Presione Enter para continuar...")
    system("cls")
