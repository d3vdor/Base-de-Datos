import os

def comprobar_lista(lista):
    if (len(lista) == 0):
        return True

def mostrar_usuarios(lista_usuarios,nombre_buscar):
    os.system("clear")
    lista_llena = comprobar_lista(lista_usuarios)

    encontrado = False
    if not lista_llena:
        encontrado = False
    
    # Encabezado fuera del ciclo para que no se repita por cada usuario
        print("\n\t{:<8} {:<10} {:<15} {:<15}".format("ID", "Nombre", "Ap. Paterno", "Ap. Materno"))
        print("\t" + "-"*50)

        for id_bd, nombre, ap, am, fn, dir in lista_usuarios:
            if ( nombre.lower() == nombre_buscar.lower() ): # mantener ambos nombres en minuscula
                print(f"\t{id_bd:<8} {nombre:<10} {ap:<15} {am:<15}")
                encontrado = True
                
        if not encontrado:
            print(f"\nNo existe el nombre: {nombre_buscar}")

    else :
        print("No existe valores en la lista")

    return encontrado

def mostrar_todos(lista_usuarios):
    os.system("clear")

    lista_llena = comprobar_lista(lista_usuarios)
    if not lista_llena:
        print("\n\t{:<8} {:<10} {:<15} {:<15} {:<24} {:<20}".format("ID", "Nombre", "Ap. Paterno", "Ap. Materno","Fecha de nacimiento","Correo"))
        for id_bd, nombre, ap, am, fn, dir in lista_usuarios:
            print(f"\t{id_bd:<8} {nombre:<10} {ap:<15} {am:<15} {fn:<24} {dir:<20}")
    else :
        print("No existe valores en la lista")

