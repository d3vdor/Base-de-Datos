# funciones externas de python
from os import system
from time import sleep

# funciones externas del programa 
from alta import alta_usuario
from baja import baja_usuario
from mostrar_usuarios import mostrar_todos

# Menu principal
def menu_opciones():
    # lista de los usuarios que se iran agregando
    lista_usuarios = []
    while (True):
        print("\t=== Seleccione una opcion ===\n" \
            "\t1. Alta\n\t2. Baja\n\t3. Consulta\n\t4. Modificar\n\t5. Salir")
        
        # en caso de que la opcion no sea un numero se muestra el errro al usuario
        try:
            opc = int(input("\t\nSeleccione una opcion: "))
        except ValueError:
            print("La opcion debe de ser un numero entero entre el 1 al 5")
            continue # regresamos al scoop del while

        # opciones del menu
        if (opc == 1):
            nuevo_usuario = alta_usuario()
            lista_usuarios.append(nuevo_usuario) # agrega el usuario a la lista de usuarios
            print(lista_usuarios)
        elif (opc == 2):
            baja_usuario(lista_usuarios)
        elif (opc == 3):
            mostrar_todos(lista_usuarios)
        elif (opc == 5):
            print("Cerrando programa")
            sleep(3)
            system('clear')
            print("Vuelva pronto :D")
            break
            
