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
    




if __name__ == '__main__':
    main()