# ... existing code ...
def input_number_in_range(prompt, min_value, max_value, is_float=False):
    while True:
        try:
            value = input(prompt)
            value = float(value) if is_float else int(value)
            if value < min_value or value > max_value:
                print(f"Value must be between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid number. Please try again.")
# ... existing code ...
def register_sale():
    print("\n--- Register Sale ---")
    client = input_non_empty("Client name: ")
    title = input_non_empty("Product title: ")
    product = find_product(title)
    if not product:
        print("Product not found.")
        return
    if product["stock"] == 0:
        print("No stock available for this product.")
        return
    quantity = input_positive_number("Quantity: ")
    if quantity > product["stock"]:
        print("Insufficient stock.")
        return
    discount = input_number_in_range("Discount percentage (0-100, 0 if none): ", 0, 100, is_float=True)
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sale = {
        "client": client,
        "product_title": product["title"],
        "quantity": quantity,
        "date": date,
        "discount": discount
    }
    sales.append(sale)
    product["stock"] -= quantity
    print("Sale registered successfully.")
# ... existing code ... Manual de Usuario - Sistema de Gestión de Estudiantes

Este manual describe cómo utilizar el programa de gestión de información académica para estudiantes.

 1. Introducción

Este programa en Python permite a los usuarios registrar, consultar, actualizar y eliminar la información académica de los estudiantes de una institución educativa. Es una herramienta útil para gestionar datos como el nombre, número de identificación, edad y notas de los estudiantes.

 2. Requisitos

Para ejecutar este programa, necesitará tener Python instalado en su sistema (versión 3.x recomendada).

 3. Cómo Ejecutar el Programa

1.  **Guarde el archivo**: Guarde el código proporcionado como `gestion_estudiantes.py`.
2.  **Abra una terminal/símbolo del sistema**: Navegue hasta el directorio donde guardó el archivo.
3.  **Ejecute el programa**: Escriba el siguiente comando y presione Enter:
    ```bash
    python gestion_estudiantes.py
    ```

 4. Menú Principal

Una vez que el programa se inicie, se le presentará el siguiente menú de opciones:

--- Gestión de Estudiantes ---

Registrar estudiante

Consultar estudiante

Actualizar notas

Eliminar estudiante

Ver todos los estudiantes

Salir

Seleccione una opción:


Para interactuar con el programa, ingrese el número correspondiente a la opción que desea realizar y presione Enter.

 5. Opciones del Programa

A continuación, se detalla cada una de las opciones disponibles en el menú:

Registrar estudiante

Esta opción le permite añadir un nuevo estudiante al sistema.

* **Pasos**:
    1.  Ingrese `1` en el menú principal y presione Enter.
    2.  Se le pedirá que ingrese el **número de identificación** del estudiante. Este debe ser único. Si intenta ingresar una identificación ya existente, el sistema le informará y le pedirá una nueva.
    3.  Ingrese el **nombre** del estudiante.
    4.  Ingrese la **edad** del estudiante (debe ser un número entero positivo).
    5.  [cite_start]Se le preguntará **cuántas notas** desea ingresar (mínimo 3)[cite: 6].
    6.  Ingrese cada nota individualmente. Las notas deben estar en una escala de 0 a 5.
* **Ejemplo**:
    ```
    --- Registrar Estudiante ---
    Ingrese el número de identificación del estudiante: 12345
    Ingrese el nombre del estudiante: Ana García
    Ingrese la edad del estudiante: 20
    ¿Cuántas notas desea ingresar (mínimo 3)? 4
    Ingrese la nota 1: 4.5
    Ingrese la nota 2: 3.8
    Ingrese la nota 3: 5.0
    Ingrese la nota 4: 4.2
    Estudiante 'Ana García' registrado exitosamente.
    ```

 Consultar estudiante

Esta opción le permite buscar y ver la información de un estudiante específico utilizando su número de identificación.

* **Pasos**:
    1.  Ingrese `2` en el menú principal y presione Enter.
    2.  Ingrese el **número de identificación** del estudiante que desea consultar.
* **Resultados**:
    * Si el estudiante existe, se mostrará su nombre, identificación, edad, la lista de sus notas y su promedio.
    * Si el estudiante no existe, se mostrará un mensaje indicando que no se encontró al estudiante.
* **Ejemplo**:
    ```
    --- Consultar Estudiante ---
    Ingrese el número de identificación del estudiante a consultar: 12345

    --- Información del Estudiante ---
    Nombre: Ana García
    Identificación: 12345
    Edad: 20
    Notas: 4.5, 3.8, 5.0, 4.2
    Promedio: 4.38
    ```

 3. Actualizar notas

Esta opción le permite modificar la lista de notas de un estudiante existente.

* **Pasos**:
    1.  Ingrese `3` en el menú principal y presione Enter.
    2.  Ingrese el **número de identificación** del estudiante cuyas notas desea actualizar.
    3.  Se le preguntará **cuántas nuevas notas** desea ingresar (mínimo 3).
    4.  Ingrese cada nueva nota.
* **Resultados**:
    * Si el estudiante existe, sus notas se actualizarán con las nuevas notas ingresadas.
    * Si el estudiante no existe, se mostrará un mensaje indicando que no se encontró al estudiante.
* **Ejemplo**:
    ```
    --- Actualizar Notas ---
    Ingrese el número de identificación del estudiante para actualizar notas: 12345
    Notas actuales de Ana García: 4.5, 3.8, 5.0, 4.2
    ¿Cuántas notas nuevas desea ingresar para Ana García (mínimo 3)? 3
    Ingrese la nueva nota 1: 4.0
    Ingrese la nueva nota 2: 3.5
    Ingrese la nueva nota 3: 4.8
    Notas del estudiante 'Ana García' actualizadas exitosamente.
    ```

 4. Eliminar estudiante

Esta opción le permite remover por completo el registro de un estudiante del sistema.

* **Pasos**:
    1.  Ingrese `4` en el menú principal y presione Enter.
    2.  Ingrese el **número de identificación** del estudiante que desea eliminar.
* **Resultados**:
    * Si el estudiante existe, su registro será eliminado y se mostrará un mensaje de confirmación.
    * Si el estudiante no existe, se mostrará un mensaje indicando que no se encontró al estudiante.
* **Ejemplo**:
    ```
    --- Eliminar Estudiante ---
    Ingrese el número de identificación del estudiante a eliminar: 12345
    Estudiante 'Ana García' con identificación '12345' eliminado exitosamente.
    ```

  5. Ver todos los estudiantes

Esta opción muestra una lista de todos los estudiantes actualmente registrados en el sistema, junto con sus datos y su promedio general.

* **Pasos**:
    1.  Ingrese `5` en el menú principal y presione Enter.
* **Resultados**:
    * Si hay estudiantes registrados, se mostrará una lista formatada de cada estudiante.
    * Si no hay estudiantes registrados, se mostrará un mensaje indicándolo.
* **Ejemplo**:
    ```
    --- Listado General de Estudiantes ---
    Identificación: 67890
    Nombre: Juan Pérez
    Edad: 22
    Notas: 3.0, 4.0, 3.5
    Promedio: 3.50
    -----------------------------------
    Identificación: 11223
    Nombre: María López
    Edad: 19
    Notas: 4.2, 4.8, 3.9, 4.5
    Promedio: 4.35
    -----------------------------------
    ```

 6. Salir

Esta opción finaliza la ejecución del programa.

* **Pasos**:
    1.  Ingrese `6` en el menú principal y presione Enter.
* **Resultados**:
    * El programa mostrará un mensaje de despedida y se cerrará.

Consideraciones Adicionales

* **Validación de Entradas**: El programa incluye validaciones básicas para asegurarse de que los datos ingresados sean del tipo correcto y cumplan con ciertos requisitos (ej. edad positiva, notas entre 0 y 5, mínimo 3 notas).
* **Permanencia de Datos**: Los datos de los estudiantes se almacenan en la memoria mientras el programa se está ejecutando. Si el programa se cierra, todos los datos se perderán. Para una aplicación real, se necesitaría implementar almacenamiento persistente (por ejemplo, en un archivo o base de datos).
* **Comentarios en el Código**: El código fuente (`gestion_estudiantes.py`) está comentado para facilitar su comprensión y mantenimiento 
