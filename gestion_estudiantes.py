# gestion_estudiantes.py

def mostrar_menu():
    #Muestra el menú principal de opciones al usuario.
    print("Gestión de Estudiantes")
    print("1. Registrar estudiante")
    print("2. Consultar estudiante")
    print("3. Actualizar notas")
    print("4. Eliminar estudiante")
    print("5. Ver todos los estudiantes")
    print("6. Salir")
    print("------------------------------")

def registrar_estudiante(estudiantes):
    #Permite registrar un nuevo estudiante en el sistema
    print("Registrar Estudiante")
    while True:
        identificacion = input("Ingrese el número de identificación del estudiante: ").strip()
        if not identificacion:
            print("La identificación no puede estar vacía. Inténtelo de nuevo.")
        elif identificacion in estudiantes:
            print("Ya existe un estudiante con esta identificación. Intente con otra.")
        else:
            break

    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío. Inténtelo de nuevo.")
        else:
            break

    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if edad <= 0:
                print("La edad debe ser un número positivo. Inténtelo de nuevo.")
            else:
                break
        except ValueError:
            print("Edad inválida. Por favor, ingrese un número entero.")

    notas = []
    while True:
        try:
            num_notas = int(input("¿Cuántas notas desea ingresar (mínimo 3)? "))
            if num_notas < 3:
                print("Debe ingresar al menos 3 notas.")
            else:
                break
        except ValueError:
            print("Número de notas inválido. Por favor, ingrese un número entero.")

    for i in range(num_notas):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i + 1}: "))
                if 0 <= nota <= 5: # Asumiendo una escala de 0 a 5
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 5. Inténtelo de nuevo.")
            except ValueError:
                print("Nota inválida. Por favor, ingrese un número.")

    estudiantes[identificacion] = {
        "nombre": nombre,
        "edad": edad,
        "notas": notas
    }
    print(f"Estudiante '{nombre}' registrado exitosamente.")

def calcular_promedio(notas):
    #Calcula el promedio de una lista de notas.
    if not notas:
        return 0
    return sum(notas) / len(notas)

def consultar_estudiante(estudiantes):
    #Consulta la información de un estudiante por su número de identificación.
    print("Consultar Estudiante")
    identificacion = input("Ingrese el número de identificación del estudiante a consultar: ").strip()

    if identificacion in estudiantes:
        estudiante = estudiantes[identificacion]
        print(f"Información del Estudiante")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Identificación: {identificacion}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Notas: {', '.join(map(str, estudiante['notas']))}")
        print(f"Promedio: {calcular_promedio(estudiante['notas']):.2f}")
    else:
        print(f"El estudiante con identificación '{identificacion}' no se encontró.")

def actualizar_notas(estudiantes):
    #Permite modificar las notas de un estudiante existente.
    print("Actualizar Notas")
    identificacion = input("Ingrese el número de identificación del estudiante para actualizar notas: ").strip()

    if identificacion in estudiantes:
        estudiante = estudiantes[identificacion]
        print(f"Notas actuales de {estudiante['nombre']}: {', '.join(map(str, estudiante['notas']))}")
        
        nuevas_notas = []
        while True:
            try:
                num_notas = int(input(f"¿Cuántas notas nuevas desea ingresar para {estudiante['nombre']} (mínimo 3)? "))
                if num_notas < 3:
                    print("Debe ingresar al menos 3 notas.")
                else:
                    break
            except ValueError:
                print("Número de notas inválido. Por favor, ingrese un número entero.")

        for i in range(num_notas):
            while True:
                try:
                    nota = float(input(f"Ingrese la nueva nota {i + 1}: "))
                    if 0 <= nota <= 5:
                        nuevas_notas.append(nota)
                        break
                    else:
                        print("La nota debe estar entre 0 y 5. Inténtelo de nuevo.")
                except ValueError:
                    print("Nota inválida. Por favor, ingrese un número.")
        
        estudiante['notas'] = nuevas_notas
        print(f"Notas del estudiante '{estudiante['nombre']}' actualizadas exitosamente.")
    else:
        print(f"El estudiante con identificación '{identificacion}' no se encontró.")

def eliminar_estudiante(estudiantes):
    #Permite eliminar un registro de estudiante.
    print("Eliminar Estudiante")
    identificacion = input("Ingrese el número de identificación del estudiante a eliminar: ").strip()

    if identificacion in estudiantes:
        nombre_estudiante = estudiantes[identificacion]['nombre']
        del estudiantes[identificacion]
        print(f"Estudiante '{nombre_estudiante}' con identificación '{identificacion}' eliminado exitosamente.")
    else:
        print(f"El estudiante con identificación '{identificacion}' no se encontró.")

def ver_todos_los_estudiantes(estudiantes):
    #Muestra una lista de todos los estudiantes registrados y su promedio general
    print("\n Listado General de Estudiantes")
    if not estudiantes:
        print("No hay estudiantes registrados aún.")
        return

    for identificacion, estudiante in estudiantes.items():
        promedio = calcular_promedio(estudiante['notas'])
        print(f"Identificación: {identificacion}")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Notas: {', '.join(map(str, estudiante['notas']))}")
        print(f"Promedio: {promedio:.2f}")
        print("")

def main():
    #Función principal que ejecuta el programa de gestión de estudiantes
    estudiantes = {} # Diccionario para almacenar los estudiantes

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            registrar_estudiante(estudiantes)
        elif opcion == '2':
            consultar_estudiante(estudiantes)
        elif opcion == '3':
            actualizar_notas(estudiantes)
        elif opcion == '4':
            eliminar_estudiante(estudiantes)
        elif opcion == '5':
            ver_todos_los_estudiantes(estudiantes)
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    main()