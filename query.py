from datetime import date
import mysql.connector


db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="web_scrapping_bgg")
cursor = db_connection.cursor()

def insert_data(name, year, popularity, best_for, weight):  
  try:  
    cursor = db_connection.cursor()
    sql = "INSERT INTO bg (bg_name, year, popularity, best_for, weight) VALUES (%s, %s, %s, %s, %s)"
    values = (name, year, popularity, best_for, weight)
    cursor.execute(sql, values)
    db_connection.commit()
  except mysql.connector.Error as err:
    print(f"Something went wrong: {err}")

cursor.close()
