import re
import mysql.connector

def eliminar():
    # Establecer la conexión a la base de datos
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='Ropa')

    # Verificar si la conexión está establecida
    if cnx and cnx.is_connected():
        try:
            # Obtener detalles de la eliminación del usuario
            print("Introduce el nombre de la tabla")
            Tabla = input()
            pattern = re.compile("[^ ]")
            matches = re.findall(pattern, Tabla)
            Tabla = ''.join(matches)

            print("Introduce el Product id")
            match = []
            Product_id = None 
            pattern2 = re.compile("[0-9]")
            while not match:
                Product_id = input()
                match = re.findall(pattern2, Product_id)

            # Crear y ejecutar la consulta SQL para eliminar el registro
            query = f"DELETE FROM {Tabla} WHERE Product_id = {Product_id};"
            with cnx.cursor() as cursor:
                cursor.execute(query)

            # Confirmar los cambios realizados
            cnx.commit()
            print("Eliminación exitosa")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # Cerrar la conexión
            cnx.close()

    else:
        print("Could not connect")

def actualizar():
    # Establecer la conexión a la base de datos
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='Ropa')

    # Verificar si la conexión está establecida
    if cnx and cnx.is_connected():
        try:
            # Obtener detalles de la actualización del usuario
            print("Introduce el nombre de la tabla")
            Tabla = input()
            pattern = re.compile("[^ ]")
            matches = re.findall(pattern, Tabla)
            Tabla = ''.join(matches)

            print("Introduce el Product id")
            Verdad = True
            pattern2 = re.compile("[0-9]")
            Product_id = None
            while Verdad:
                try:
                    Product_id = input()
                    matches2 = re.findall(pattern2, Product_id)
                    respuesta1 = ''.join(matches2)
                    Product_id = int(respuesta1)
                    if isinstance(Product_id, int):
                        Verdad = False
                except ValueError:
                    print("Ingresa un id válido")

            # Resto de tu código...

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # Cerrar la conexión
            cnx.close()

    else:
        print("Could not connect")


def insertarempleados():
    # Establecer la conexión a la base de datos
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='Ropa')

    # Verificar si la conexión está establecida
    if cnx and cnx.is_connected():
        try:
            # Obtener detalles de la actualización del usuario
            print("Introduce el nombre de la tabla")
            Tabla = input()

            print("Introduce el Product id")
            Product_id = None
            value1 = True
            while value1:
                try:
                    respuesta1 = input()
                    Product_id = int(respuesta1)
                    if isinstance(Product_id, int):
                        value1 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el nombre del empleado")
            nombre_empleado = None
            value2 = True
            while value2:
                try:
                    respuesta_nombre = input()
                    if respuesta_nombre.replace(" ", "").isalpha():
                        nombre_empleado = respuesta_nombre
                        value2 = False
                    else:
                        print("Ingresa un nombre válido (solo letras y espacios)")
                except ValueError:
                    print("Error al procesar la entrada. Ingresa un nombre válido.")

            print("Introduce el color (Número entero)")
            color = None
            value3 = True
            while value3:
                try:
                    respuesta3 = input()
                    color = int(respuesta3)
                    if isinstance(color, int):
                        value3 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el sexo (Número entero)")
            sexo = None
            value4 = True
            while value4:
                try:
                    respuesta4 = input()
                    sexo = int(respuesta4)
                    if isinstance(sexo, int):
                        value4 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el temp_id (Número entero)")
            temp = None
            value5 = True
            while value5:
                try:
                    respuesta5 = input()
                    temp = int(respuesta5)
                    if isinstance(temp, int):
                        value5 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el Pais (Número entero)")
            pais = None
            value6 = True
            while value6:
                try:
                    respuesta6 = input()
                    pais = int(respuesta6)
                    if isinstance(pais, int):
                        value6 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id de la sucursal (Número entero)")
            suc = None
            value7 = True
            while value7:
                try:
                    respuesta7 = input()
                    suc = int(respuesta7)
                    if isinstance(suc, int):
                        value7 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id de la rec (Número entero)")
            rec = None
            value8 = True
            while value8:
                try:
                    respuesta8 = input()
                    rec = int(respuesta8)
                    if isinstance(rec, int):
                        value8 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id del departamento (Número entero)")
            dep = None
            value9 = True
            while value9:
                try:
                    respuesta9 = input()
                    dep = int(respuesta9)
                    if isinstance(dep, int):
                        value9 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id del com (Número entero)")
            Com = None
            value10 = True
            while value10:
                try:
                    respuesta10 = input()
                    Com = int(respuesta10)
                    if isinstance(Com, int):
                        value10 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id del Mat (Número entero)")
            Mat = None
            value11 = True
            while value11:
                try:
                    respuesta11 = input()
                    Mat = int(respuesta11)
                    if isinstance(Mat, int):
                        value11 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id del desc (Número entero)")
            desc = None
            value12 = True
            while value12:
                try:
                    respuesta12 = input()
                    desc = int(respuesta12)
                    if isinstance(desc, int):
                        value12 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id del MS (Número entero)")
            ms = None
            value13 = True
            while value13:
                try:
                    respuesta13 = input()
                    ms = int(respuesta13)
                    if isinstance(ms, int):
                        value13 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el precio (Número decimal)")
            precio = None
            value14 = True
            while value14:
                try:
                    respuesta14 = input()
                    precio = float(respuesta14)
                    if isinstance(precio, float):
                        value14 = False
                except ValueError:
                    print("Ingresa un número decimal")

            print("Introduce la fecha")
            pattern = re.compile(r'^(20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$')
            fecha = input()
            fecha = re.findall(pattern, fecha)

            print("Introduce el id de Acepta DEV (Número entero)")
            dev = None
            value15 = True
            while value15:
                try:
                    respuesta15 = input()
                    dev = int(respuesta15)
                    if isinstance(dev, int):
                        value15 = False
                except ValueError:
                    print("Ingresa un número entero")

            # Crear y ejecutar la consulta SQL usando placeholders
            query = f"INSERT INTO {Tabla} VALUES ({Product_id}, '{nombre_empleado}', {color}, {sexo}, {temp}, {pais}, {suc}, {rec}, {dep}, {Com}, {Mat}, {desc}, {ms}, {precio}, '{fecha}', {dev})"
            with cnx.cursor() as cursor:
                cursor.execute(query)

            # Confirmar los cambios realizados
            cnx.commit()
            print("Inserción exitosa")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # Cerrar la conexión
            cnx.close()

    else:
        print("Could not connect")

def insertarVenta():
    # Establecer la conexión a la base de datos
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='Ropa')

    # Verificar si la conexión está establecida
    if cnx and cnx.is_connected():
        try:
            # Obtener detalles de la eliminación del usuario
            print("Introduce el id de la venta")
            match = []
            Venta = None 
            pattern = re.compile("[0-9]")
            while match == []:
                Venta = input()
                match = re.findall(pattern, Venta)
                Venta = ''.join(match)

            print("Introduce el Product id")
            match = []
            Product_id = None 
            pattern2 = re.compile("[0-9]")
            while match == []:
                Product_id = input()
                match = re.findall(pattern2, Product_id)
                Product_id = ''.join(match)

            print("Introduce la fecha de la venta")
            match = []
            sell = None
            while match == []:
                pattern = re.compile(r'^(20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$')
                fecha = input()
                match = re.findall(pattern, fecha)
		    
            print("Introduce el id del empleado")
            match = []
            emp_id = None 
            pattern2 = re.compile("[0-9]")
            while match == []:
                emp_id = input()
                match = re.findall(pattern2, emp_id)
                emp_id = ''.join(match)

            # Crear y ejecutar la consulta SQL para eliminar el registro
            query = f"DELETE FROM {Tabla} WHERE Product_id = {Product_id};"
            with cnx.cursor() as cursor:
                cursor.execute(query)

            # Confirmar los cambios realizados
            cnx.commit()
            print("Eliminación exitosa")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # Cerrar la conexión
            cnx.close()

    else:
        print("Could not connect")
def insertardevoluciones():
    # Establecer la conexión a la base de datos
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='Ropa')

    # Verificar si la conexión está establecida
    if cnx and cnx.is_connected():
        try:
            print("Introduce el ID de la devolución")
            match = []
            dev_id = None 
            pattern3 = re.compile("[0-9]")
            while match == []:
                dev_id = input()
                match = re.findall(pattern3, dev_id)
                dev_id = ''.join(match)

            print("Introduce el Product id")
            match = []
            Product_id = None 
            pattern2 = re.compile("[0-9]")
            while match == []:
                Product_id = input()
                match = re.findall(pattern2, Product_id)
                Product_id = ''.join(match)

            print("Introduce el sell id")
            match = []
            sell_id = None 
            pattern2 = re.compile("[0-9]")
            while match == []:
                sell_id = input()
                match = re.findall(pattern2, sell_id)
                sell_id = ''.join(match)

            print("Introduce la fecha")
            pattern = re.compile(r'^(20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$')
            fecha = input()
            fecha = re.findall(pattern, fecha)

            print("Introduce el id del empleado")
            match = []
            emp_id = None 
            pattern2 = re.compile("[0-9]")
            while match == []:
                emp_id = input()
                match = re.findall(pattern2, emp_id)
                emp_id = ''.join(match)

            # Crear y ejecutar la consulta SQL para insertar el registro
            query = f"INSERT INTO DEVOLUCIÓN VALUES ({dev_id}, {Product_id}, {sell_id}, {fecha}, {emp_id})"
            with cnx.cursor() as cursor:
                cursor.execute(query)

            # Confirmar los cambios realizados
            cnx.commit()
            print("Inserción exitosa")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # Cerrar la conexión
            cnx.close()

    else:
        print("Could not connect")

    def insertarInventario():
    # Establecer la conexión a la base de datos
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='Ropa')

    # Verificar si la conexión está establecida
    if cnx and cnx.is_connected():
        try:
            # Obtener detalles de la actualización del usuario
            print("Introduce el nombre de la tabla")
            Tabla = input()

            print("Introduce el Product id")
            Product_id = None
            res1 = None
            value1 = True
            while value1:
                try:
                    respuesta1 = input()
                    Product_id = int(respuesta1)
                    if isinstance(Product_id, int):
                        value1 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce la talla (Número entero)")
            talla = None
            res2 = None
            value2 = True
            while value2:
                try:
                    respuesta2 = input()
                    talla = int(respuesta2)
                    if isinstance(talla, int):
                        value2 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el color (Número entero)")
            color = None
            res3 = None
            value3 = True
            while value3:
                try:
                    respuesta3 = input()
                    color = int(respuesta3)
                    if isinstance(color, int):
                        value3 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce la sexo (Número entero)")
            sexo = None
            res4 = None
            value4 = True
            while value4:
                try:
                    respuesta4 = input()
                    sexo = int(respuesta4)
                    if isinstance(sexo, int):
                        value4 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el temp_id (Número entero)")
            temp = None
            res5 = None
            value5 = True
            while value5:
                try:
                    respuesta5 = input()
                    temp = int(respuesta5)
                    if isinstance(temp, int):
                        value5 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el Pais (Número entero)")
            pais = None
            res6 = None
            value6 = True
            while value6:
                try:
                    respuesta6 = input()
                    pais = int(respuesta6)
                    if isinstance(pais, int):
                        value6 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id de la sucursal (Número entero)")
            suc = None
            res7 = None
            value7 = True
            while value7:
                try:
                    respuesta7 = input()
                    suc = int(respuesta7)
                    if isinstance(suc, int):
                        value7 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id de la rec (Número entero)")
            rec = None
            res8 = None
            value8 = True
            while value8:
                try:
                    respuesta8 = input()
                    rec = int(respuesta8)
                    if isinstance(rec, int):
                        value8 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id del departamento (Número entero)")
            dep = None
            res9 = None
            value9 = True
            while value9:
                try:
                    respuesta9 = input()
                    dep = int(respuesta9)
                    if isinstance(dep, int):
                        value9 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id del com (Número entero)")
            Com = None
            res10 = None
            value10 = True
            while value10:
                try:
                    respuesta10 = input()
                    Com = int(respuesta10)
                    if isinstance(Com, int):
                        value10 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id del Mat (Número entero)")
            Mat = None
            res11 = None
            value11 = True
            while value11:
                try:
                    respuesta11 = input()
                    Mat = int(respuesta11)
                    if isinstance(Mat, int):
                        value11 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id del desc (Número entero)")
            desc = None
            res12 = None
            value12 = True
            while value12:
                try:
                    respuesta12 = input()
                    desc = int(respuesta12)
                    if isinstance(desc, int):
                        value12 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el id del MS (Número entero)")
            ms = None
            res13 = None
            value13 = True
            while value13:
                try:
                    respuesta13 = input()
                    ms = int(respuesta13)
                    if isinstance(ms, int):
                        value13 = False
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce el precio (Número decimal)")
            precio = None
            res14 = None
            value14 = True
            while value14:
                try:
                    respuesta14 = input()
                    precio = float(respuesta14)
                    if isinstance(precio, float):
                        value14 = False
                except ValueError:
                    print("Ingresa un número decimal")

            print("Introduce la fecha")
            pattern = re.compile(r'^(20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$')
            fecha = input()
            fecha = re.findall(pattern, fecha)

            print("Introduce el id de Acepta DEV (Número entero)")
            dev = None
            res15 = None
            value15 = True
            while value15:
                try:
                    respuesta15 = input()
                    dev = int(respuesta15)
                    if isinstance(dev, int):
                        value15 = False
                except ValueError:
                    print("Ingresa un número entero")

            # Crear y ejecutar la consulta SQL usando placeholders
            query = f"INSERT INTO {Tabla} VALUES ({Product_id}, {talla}, {color}, {sexo}, {temp}, {pais}, {suc}, {rec}, {dep}, {Com}, {Mat}, {desc}, {ms}, {precio}, '{fecha}', {dev})"
            with cnx.cursor() as cursor:
                cursor.execute(query)

            # Confirmar los cambios realizados
            cnx.commit()
            print("Inserción exitosa")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # Cerrar la conexión
            cnx.close()

    else:
        print("Could not connect")

print("Qué deseas hacer?")
print("1.-Eliminar un elemnto de la tabla")
print("2.-Actualizar un elemento de la tabla")
print("3.-Insertar un elemento en la tabla")

resp = 0
verdad = True
while verdad:
    try:
        intento = input()
        resp = int(intento)
        if isinstance(resp, int) and (resp < 4 and resp > 0):
            verdad = False
    except ValueError:
        print("ingresa una opción válida")

if resp == 1:
    eliminar()
elif resp == 2:
    actualizar()
else:

    print("Qué tabla deseas editar?")
    print("1.- La tabla Inventario")
    print("2.- La tabla Empleados")
    print("3.- La tabla Ventas")
    print("4.- La tabla devoluciones")
    
    resp = 0
    verdad = True
    while verdad:
        try:
            intento = input()
            resp = int(intento)
            if isinstance(resp, int) and (resp< 5 and resp > 0):
                verdad = False
            else:
                print("Ingresa una opción válida")
        except ValueError:
            print("ingresa una opción válida")
    
    if resp == 1:
        insertarInventario()
    elif resp == 2:
        insertarempleados()
    elif resp == 3:
        insertarVenta()
    else:
        insertardevoluciones()
