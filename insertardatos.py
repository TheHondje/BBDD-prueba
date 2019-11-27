import sqlite3


def main():
    """insertar nuevos elementos"""
    conn=sqlite3.connect("PrimeraBaseD")
    cursor = conn.cursor()

    while True:
        print("Insertar productos:")
        
        nombre_articulo = input("Ingrese nombre del producto: ")
        precio= input("Ingrese precio: ")
        seccion= input("Ingrese seccion: ")
        

        cursor.execute(
            "INSERT INTO productos VALUES (NULL,?,?,?)",
            (nombre_articulo, precio, seccion)
            )
        conn.commit()
        print("producto ingresado")
        r = input("Desea ingresar un nuevo producto? (s/n):")
        if r == "s":
            continue
        else:
            break

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