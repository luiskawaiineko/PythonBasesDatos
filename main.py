#python -m pip install mysql-connector-python
import mysql.connector
print("Conectando a la base de datos. Por favor, espere...")
mydb = mysql.connector.connect(
  host="dam2.mysql.iesquevedo.es",
  user="root",
  password="quevedo2020",
  database="Volpre_Luismi",
  port="3335", 
)
print("Conexión realizada con éxito!")
producto = str.upper(input("Introduce un producto:\n"))
kilos = input("Introduce cantidad de kilos:\n")
mycursor = mydb.cursor()
print("Calculando mejor precio. Por favor, espere...")
#mycursor.execute("SELECT Descripción_Origen,MIN(Precio_Mínimo) FROM volpre2019 where Descripción_Variedad ='"+producto+"'")
mycursor.execute("select Descripción_Origen,Kilos,Precio_Mínimo from volpre2019 where Descripción_Variedad ='"+producto+"' ORDER BY Precio_Mínimo ASC LIMIT 1")
#mycursor.execute("SELECT * FROM volpre2019 where Descripción_Variedad ='"+producto+"'")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)