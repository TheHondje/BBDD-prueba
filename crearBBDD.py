import sqlite3


def main():
	"""crear BB.DD"""
	conn=sqlite3.connect("PrimeraBaseD")

	Cursor=conn.cursor()

	Cursor.execute("CREATE TABLE PRODUCTOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE TEXT(40), PRECIO NUMERIC, SECCION TEXT(20))")

	print("base de datos creada")

	conn.close()




if __name__ == "__main__":
    main()

