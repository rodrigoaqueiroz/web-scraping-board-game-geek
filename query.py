from datetime import date
from tkinter import INSERT
import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="web_scrapping_bgg")
cursor = db_connection.cursor()

# sql = "INSERT INTO user (name, cpf) VALUES ('adsa', '000s.000.000.00')"
# cursor.execute(sql)


def insert_data(name, year, popularity):    
  cursor = db_connection.cursor()
  sql = "INSERT INTO bg (bg_name, year, popularity) VALUES (%s, %s, %s)"
  values = (name, year, popularity)
  cursor.execute(sql, values)
  db_connection.commit()


cursor.close()
# db_connection.commit()
# db_connection.close()