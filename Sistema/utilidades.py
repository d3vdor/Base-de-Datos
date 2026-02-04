from datetime import datetime
import os

# Validar que la fecha de cumpleaños este bien escrita
def validar_fecha(texto):
    while True:
        fecha = input(f"{texto} (DD/MM/AAAA): ")
        try:
            fecha_final = datetime.strptime(fecha, "%d/%m/%Y")
            return fecha_final.date()
        except ValueError:
            print("El formato de la fecha es (DD/MM/AAAA)")

# Validar un campo para que sea del tipo deseado
def validar_campo(texto,tipo_de_dato,nombre_tipo):
    while True:
        entrada = input(f"{texto}")
        try:
            validado = tipo_de_dato(entrada)
            return validado
        except ValueError:
            print(f"Error: el campo debe de ser de tipo {nombre_tipo}")

# Comprobar que la lista esta vacia
def comprobar_lista(lista):
    if (len(lista) == 0):
        return True

# Detecta si el nombre buscado existe en la lista (retorna True o False)
def mostrar_usuarios(lista_usuarios,nombre_buscar):
    os.system("clear")
    lista_llena = comprobar_lista(lista_usuarios)

    encontrado = False
    if not lista_llena:
        encontrado = False
    
    # Encabezado fuera del ciclo para que no se repita por cada usuario
        print("\n\t{:<8} {:<15} {:<15} {:<15}".format("ID", "Nombre", "Ap. Paterno", "Ap. Materno"))
        print("\t" + "-"*50)

        for id_bd, nombre, ap, am, fn, dir in lista_usuarios:
            if ( nombre.lower() == nombre_buscar.lower() ): # mantener ambos nombres en minuscula
                print(f"\t{id_bd:<8} {nombre:<15} {ap:<15} {am:<15}")
                encontrado = True
                
        if not encontrado:
            print(f"\nNo existe el nombre: {nombre_buscar}")

    else :
        print("No existe valores en la lista")

    return encontrado

# Muestra todos los usuarios de la base
def mostrar_todos(lista_usuarios):
    os.system("clear")

    # comprobar que hay usuarios dentro de la lista
    lista_vacia = comprobar_lista(lista_usuarios)
    if not lista_vacia:
        print("\n\t{:<8} {:<15} {:<15} {:<15} {:<24} {:<20}".format("ID", "Nombre", "Ap. Paterno", "Ap. Materno","Fecha de nacimiento","Correo"))
        for id_bd, nombre, ap, am, fn, dir in lista_usuarios:
            fecha_formato = fn.strftime("%d/%m/%Y")
            print(f"\t{id_bd:<8} {nombre:<15} {ap:<15} {am:<15} {fecha_formato:<24} {dir:<20}")
    else :
        print("No existe valores en la lista")

# Muestra a todos los usuarios que tengan ese nombre
def mostrar_por_nombre(lista_usuario,nombre_user):
    lista_vacia = comprobar_lista(lista_usuario)

    if not lista_vacia:
        print("\n\t{:<8} {:<15} {:<15} {:<15} {:<24} {:<20}".format("ID", "Nombre", "Ap. Paterno", "Ap. Materno","Fecha de nacimiento","Correo"))
        for id_bd, nombre, ap, am, fn, dir in lista_usuario:
            if (nombre.lower() == nombre_user.lower()):
                fecha_formato = fn.strftime("%d/%m/%Y")
                print(f"\t{id_bd:<8} {nombre:<15} {ap:<15} {am:<15} {fecha_formato:<24} {dir:<20}")
    else:
        print("Nombre de usuario no encontrado")

# Mostrar por id
def mostrar_por_id(lista_usuario,id_user):
    lista_vacia = comprobar_lista(lista_usuario)

    if not lista_vacia:
        print("\n\t{:<8} {:<15} {:<15} {:<15} {:<24} {:<20}".format("ID", "Nombre", "Ap. Paterno", "Ap. Materno","Fecha de nacimiento","Correo"))
        for id_bd, nombre, ap, am, fn, dir in lista_usuario:
            if (id_bd == id_user):
                fecha_formato = fn.strftime("%d/%m/%Y")
                print(f"\t{id_bd:<8} {nombre:<15} {ap:<15} {am:<15} {fecha_formato:<24} {dir:<20}")
    else:
        print("Nombre de usuario no encontrado")       


# guardar informacion en archvio .txt
def guardar_archivo(lista_usuarios, nombre_archivo="usuarios.txt"):
    try:
        with open(nombre_archivo, "w") as archivo:
            for u in lista_usuarios:
                linea = f"{u[0]},{u[1]},{u[2]},{u[3]},{u[4].strftime('%d/%m/%Y')},{u[5]}\n"
                archivo.write(linea)
        print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar: {e}")

# cargar el .txt
def cargar_archivo(nombre_archivo="usuarios.txt"):
    lista_temporal = []
    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if datos:
                    id_bd = int(datos[0])
                    nombre = datos[1]
                    ap = datos[2]
                    am = datos[3]
                    fn = datetime.strptime(datos[4], "%d/%m/%Y")
                    correo = datos[5]
                    
                    lista_temporal.append([id_bd, nombre, ap, am, fn, correo])
    except FileNotFoundError:
        # Si el archivo no existe, creamos uno vacío
        open(nombre_archivo, "w").close()
    return lista_temporal