# funciones externas de python
from os import system
from time import sleep

# funciones externas del programa 
from alta import alta_usuario
from baja import baja_usuario
from utilidades import mostrar_todos
from modificar_usuario import modificar_usuario
from utilidades import cargar_archivo
from utilidades import guardar_archivo

# Menu principal
def menu_opciones():
    system("clear")
    # lista de los usuarios que se iran agregando
    lista_usuarios = cargar_archivo()
    while (True):
        print("=== Seleccione una opcion ===\n" \
            "1. Alta\n2. Baja\n3. Consulta\n4. Modificar\n5. Salir")
        
        # en caso de que la opcion no sea un numero se muestra el errro al usuario
        try:
            opc = int(input(" \nSeleccione una opcion: "))
        except ValueError:
            print("La opcion debe de ser un numero entero entre el 1 al 5")
            continue # regresamos al scoop del while

        # opciones del menu
        if (opc == 1):
            nuevo_usuario = alta_usuario()
            lista_usuarios.append(nuevo_usuario) # agrega el usuario a la lista de usuarios
            print(lista_usuarios)
            guardar_archivo(lista_usuarios)
        elif (opc == 2):
            baja_usuario(lista_usuarios)
            guardar_archivo(lista_usuarios)
        elif (opc == 3):
            mostrar_todos(lista_usuarios)
        elif (opc == 4):
            modificar_usuario(lista_usuarios)
            guardar_archivo(lista_usuarios)
        elif (opc == 5):
            print("Vuelva pronto :D")
            system('clear')
            break
        else:
            print("Escoja un numero del 1 al 5")
            
