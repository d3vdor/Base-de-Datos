# funciones de python
from os import system

# funciones del programa
from utilidades import mostrar_todos
from utilidades import mostrar_por_nombre
from utilidades import mostrar_por_id
from utilidades import validar_campo
from utilidades import validar_fecha


def menu_modificar(lista,id_user):
    print("=== Modificar ===\n")
    print("1. Nombre\n2. Apellido Paterno\n3. Apellido Materno\n4. Fecha de Nacimiento\n5. Direccion")
    opc = validar_campo("Seleccione una opcion: ",int,"entero")

    # recorrer la lista y cambiar el campo de acuerdo a la opcion seleccionada
    for i in range(len(lista)):
        if((lista[i][0] == id_user) and (opc == 1)): # opcion 1: nombre
            nuevo_nombre = validar_campo("Nuevo nombre: ",str,"String")
            lista[i][1] = nuevo_nombre.capitalize()
        elif((lista[i][0] == id_user) and (opc == 2)): # opcion 2: apellido paterno
            nuevo_ap = validar_campo("Nuevo Apellido Paterno: ", str,"String")
            lista[i][2] = nuevo_ap.capitalize()
        elif((lista[i][0] == id_user) and (opc == 3)): # opcion 3: apellido materno
            nuevo_am = validar_campo("Nuevo Apellido Materno: ",str,"String")
            lista[i][3] = nuevo_am.capitalize()
        elif((lista[i][0] == id_user) and (opc == 4)): # opcion 4: fecha de nacimiento
            nueva_fn = validar_fecha("Nueva Fecha")
            lista[i][4] = nueva_fn
        elif((lista[i][0] == id_user) and (opc == 5)): # opcion 5: direccion
            nueva_dir = validar_campo("Correo nuevo: ",str,"String")
            lista[i][5] = nueva_dir
        else:
            print("Esa opcion no es valida")
    print("Datos guardados correctamente")

    

def modificar_usuario(lista):
    mostrar_todos(lista)

    # comprobar que el nombre es de tipo String
    nombre = validar_campo("Nombre a buscar: ",str,"String")
    system("clear")
    mostrar_por_nombre(lista,nombre)

    # comprobar que el id es de tipo entero
    id_user = validar_campo("ID: ", int, "Entero")
    system("clear")
    mostrar_por_id(lista,id_user)

    # mostrar menu para modificar
    menu_modificar(lista,id_user)

