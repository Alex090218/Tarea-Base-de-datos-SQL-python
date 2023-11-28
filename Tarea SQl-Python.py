import mysql.connector

def eliminar():
    cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='Ropa')

    if cnx and cnx.is_connected():
        try:
            print("Introduce el nombre de la tabla")
            Tabla = input()

            print("Introduce el Product id")
            Product_id = input()

            query = f"DELETE FROM {Tabla} WHERE Product_id = {Product_id};"
            with cnx.cursor() as cursor:
                cursor.execute(query)

            cnx.commit()
            print("Eliminación exitosa")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            cnx.close()

    else:
        print("Could not connect")

def actualizar():
    cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='Ropa')

    if cnx and cnx.is_connected():
        try:
            print("Introduce el nombre de la tabla")
            Tabla = input()

            print("Introduce el Product id")
            Product_id = input()

            print("Introduce la columna a cambiar")
            Column = input()

            print("Introduce el Nuevo valor")
            Nuevo_valor = input()

            query = f"UPDATE {Tabla} SET {Column} = %s WHERE Product_id = %s;"
            with cnx.cursor() as cursor:
                cursor.execute(query, (Nuevo_valor, Product_id))

            cnx.commit()
            print("Actualización exitosa")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            cnx.close()

    else:
        print("Could not connect")

def insertar():
    cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='Ropa')

    if cnx and cnx.is_connected():
        try:
            print("Introduce el nombre de la tabla")
            Tabla = input()

            print("Introduce el Product id")
            Product_id = None
            while True:
                try:
                    respuesta1 = input()
                    Product_id = int(respuesta1)
                    break
                except ValueError:
                    print("Ingresa un número entero")

            print("Introduce la talla (Número entero)")
            talla = None
            while True:
                try:
                    respuesta2 = input()
                    talla = int(respuesta2)
                    break
                except ValueError:
                    print("Ingresa un número entero")

            # Resto del código...

            query = f"INSERT INTO {Tabla} VALUES ({Product_id}, {talla}, {color}, {sexo}, {temp}, {pais}, {suc}, {rec}, {dep}, {Com}, {Mat}, {desc}, {ms}, {precio}, '{fecha}', {dev})"
            with cnx.cursor() as cursor:
                cursor.execute(query)

            cnx.commit()
            print("Inserción exitosa")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            cnx.close()

    else:
        print("Could not connect")

value = True
filt = None
while value:
    print("Qué deseas hacer?")
    print("1.-Eliminar un elemento de la tabla")
    print("2.-Actualizar un elemento de la tabla")
    print("3.-Ingresar un valor a la tabla")
    try:
        respuesta = input()
        filt = int(respuesta)
        if isinstance(filt, int) and (filt > 0 and filt < 4):
            value = False
            print("Opción válida.")
        else:
            print("Ingresa una opción válida.")

    except ValueError:
        print("Ingresa una opción válida.")

if filt == 1:
    eliminar()
elif filt == 2:
    actualizar()
else:
    insertar()

