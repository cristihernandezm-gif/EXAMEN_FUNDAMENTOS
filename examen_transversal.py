def mostrar_menu():
    print("""
========== MENÚ PRINCIPAL ==========
1. Cupos por tipo de plan
2. Búsqueda de planes por rango de precio
3. Actualizar precio de plan
4. Agregar plan
5. Eliminar plan
6. Salir
=====================================
          """)

def obtener_opcion():
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 6:
            print("Opción no válida, seleccione una opción del menú.")
    except ValueError:
        print("Opción no válida, seleccione una opción del menú.")
    return opcion

def val_codigo(codigo):
    if codigo not in planes and codigo not in inscripciones:
        return True
    else:
        return False

def val_nombre(nombre):
    if nombre.strip() and len(nombre) != 0:
        return True
    else:
        return False

def val_precio(precio):
    try:
        precio = float(precio)
        if precio > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def val_cupos(cupos):
    try:
        cupos = int(cupos)
        if cupos >= 0:
            return True
        else:
            return False
    except ValueError:
        return False

def val_duracion(duracion):
    try:
        duracion=int(duracion)
        if duracion > 0 and len(duracion) != 0:
            return True
        else:
            return False
    except ValueError:
        return False
    
def val_horario(horario):
    if horario in ['mañana', 'tarde', 'noche', 'libre']:
        return True
    else:
        return False

def val_tipo(tipo):
    if tipo.strip().lower() in ['mensual', 'trimestral', 'anual']:
        return True
    else:
        return False

def acceso_piscina(acceso):
    if acceso.strip().lower() == 's':
        return True
    elif acceso.strip().lower() == 'n':
        return False
    else:
        return False

def incluye_clases(incluye):
    if incluye.strip().lower() == 's':
        return True
    elif incluye.strip().lower() == 'n':
        return False
    else:
        return False
#Recibe el tipo de plan como parámetro, no retorna ningún valor y muestra el resultado directamente por pantalla
def cupos_tipo(tipo_buscar):
    for posi, plan in planes.items():
        if plan[1] == tipo_buscar:
            return inscripciones[posi][1]

def buscar_codigo(codigo):
    for cod, plan in planes.items():
        if cod == codigo:
            return True
    return False

def busqueda_precio(precio_min, precio_max, codigo, plan):
    if precio_min <= precio_max:
        print(f"Código: {codigo}, Nombre: {plan[0]}, Precio: ${precio_plan}")

def agregar_plan(codigo, nombre, duracion, cupos, acceso_piscina, incluye_clases, horario):
    planes[codigo] = [nombre, duracion, cupos, acceso_piscina, incluye_clases, horario]
    inscripciones[codigo] = [0, cupos]

    print(f"Plan {nombre} agregado exitosamente.")

planes = {

'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
'F003': ['Plan Estudiante', 'trimestral', 3, False, True,'tarde'],
'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],

}

inscripciones = {

'F001': [14990, 30],
'F002': [22990, 10],
'F003': [39990, 0],
'F004': [35990, 6],
'F005': [159990, 2],
'F006': [18990, 15],

}


while True:
    mostrar_menu()
    op = obtener_opcion()
    #cupos por tipo de plan
    if op == 1:
        busco_cupos_plan =  input("Ingrese el plan para ver los cupos disponibles(mensual,trimestral,anual): ")
        cupos_disponibles = cupos_tipo(busco_cupos_plan)
        print(f"Cupos disponibles para el plan {busco_cupos_plan}: {cupos_disponibles}")
    elif op == 2:
    #busqueda de planes por rango de precio
        precio_min = float(input("Ingrese el precio mínimo: "))
        precio_max = float(input("Ingrese el precio máximo: "))
        for codigo, plan in planes.items():
            precio_plan = inscripciones[codigo][0]
            if precio_min <= precio_plan <= precio_max:
                busqueda_precio(precio_min, precio_max, codigo, plan)

            
    elif op == 3:
    #Actualizar precio de plan
        codigo_plan = input("Ingrese el código del plan a actualizar: ")
        if codigo_plan in inscripciones:
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            inscripciones[codigo_plan][0] = nuevo_precio
            print(f"Precio del plan {planes[codigo_plan][0]} actualizado a ${nuevo_precio}")
        else:
            print("Código de plan no válido.")
        
        precio_again=input("desea actualizar otro precio? (s/n): ")
        if precio_again.lower() == 's':
            continue
        else:
            print("Saliendo de la actualización de precios.")
    elif op == 4:
    #Agregar plan
        codigo_nuevo = input("Ingrese el código del nuevo plan: ")
        if val_codigo(codigo_nuevo):
            nombre_nuevo = input("Ingrese el nombre del nuevo plan: ")
            tipo_nuevo = input("Ingrese el tipo de plan (mensual/trimestral/anual): ")
            val_duracion_nuevo = input("Ingrese la duración del nuevo plan: ")
            horario_nuevo = input("Ingrese el horario (mañana/tarde/noche/libre): ")
            cupos_nuevos = int(input("Ingrese la cantidad de cupos disponibles: "))
            acceso_piscina_nuevo = input("¿Incluye acceso a piscina? (s/n): ")
            incluye_clases_nuevo = input("¿Incluye clases? (s/n): ")
            precio_nuevo = float(input("Ingrese el precio del nuevo plan: "))

            vali_p=val_precio(precio_nuevo)
            vali_nombre=val_nombre(nombre_nuevo)
            vali_codigo=val_codigo(codigo_nuevo)
            vali_t=val_tipo(val_duracion_nuevo)
            vali_c=val_cupos(cupos_nuevos)
            vali_h=val_horario(horario_nuevo)
            vali_d=val_duracion(val_duracion_nuevo)
            acceso_p=acceso_piscina(acceso_piscina_nuevo)
            incluye_c=incluye_clases(incluye_clases_nuevo)

            if vali_t and vali_c and vali_h and vali_d:

                planes[codigo_nuevo] = [nombre_nuevo, val_duracion_nuevo, int(cupos_nuevos), acceso_p, incluye_c, (horario_nuevo)]
                inscripciones[codigo_nuevo] = [float(precio_nuevo), int(cupos_nuevos)]
                print(f"Plan {nombre_nuevo} agregado exitosamente.")
            elif not vali_t:
                print("Duración no válida. Debe ser mensual, trimestral o anual.")
            elif not vali_c:
                print("Cantidad de cupos no válida. Debe ser un número entero mayor o igual a 0.")
            elif not vali_h:
                print("Horario no válido. Debe ser mañana, tarde, noche o libre.")
            elif not vali_d:
                print("Duración no válida. Debe ser un número mayor a 0.")
            else:
                print("Datos no válidos. No se pudo agregar el plan.")
    elif op == 5:
    #Eliminar plan
        codigo_eliminar = input("Ingrese el código del plan a eliminar: ")
        for cod, inscripciones in inscripciones.items():
            if inscripciones[0] == codigo_eliminar:
                del planes[codigo_eliminar]
                del inscripciones[codigo_eliminar]
                print(f"Plan con código {codigo_eliminar} eliminado exitosamente.")
                break
        else:
            print("Código de plan no válido.")
                
    elif op == 6:
        print("Saliendo del programa...")
        break
