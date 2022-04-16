from datetime import date
from tkinter import INSERT
import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="bd")
cursor = db_connection.cursor()

# sql = "INSERT INTO user (name, cpf) VALUES ('adsa', '000s.000.000.00')"
# cursor.execute(sql)


def insert_data(data):    
  sql = f"INSERT INTO user (bg_name, year) VALUES ({data[0]}, {data[1]})"
  cursor.execute(sql)

cursor.close()
db_connection.commit()
db_connection.close()