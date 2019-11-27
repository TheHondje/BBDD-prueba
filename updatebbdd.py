import sqlite3


def main():
    conn=sqlite3.connect("PrimeraBaseD")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    
    productos = cursor.fetchall()
    print("Listado de productos:")
    print("---------------------------------------")
    for id, nombre_articulo, precio, seccion in productos:
        print("{} | {} | {} | {}".format(
            id, nombre_articulo, precio, seccion
        ))

    print(" ")
    print(" ")
    print("Actualizar precio: ")

    while True:
        
        id = input("Ingrese el id del articulo a actualizar: ")
        nuevo_precio = input("Ingrese el precio actualizado: ")
        cursor.execute(
            "UPDATE productos SET precio = ? where id = ?",
            (nuevo_precio, id)
        )
        r = input("Desea actualizar algun otro precio? (s/n):")
        if r == "s":
            continue
        else:
            break


    conn.commit()
    print("precio actualizado!!.")
    print(" ")

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    print("Listado de productos:")
    print("---------------------------------------")
    for id, nombre_articulo, precio, seccion in productos:
        print("{} | {} | {} | {}".format(
            id, nombre_articulo, precio, seccion
        ))

    conn.close()


if __name__ == '__main__':
    main()