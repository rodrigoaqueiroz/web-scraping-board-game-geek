from datetime import date
import mysql.connector


db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="web_scrapping_bgg")
cursor = db_connection.cursor()


def insert_data(name, year, popularity, best_for, weigth):  
  try:  
    cursor = db_connection.cursor()
    sql = "INSERT INTO bg (bg_name, year, popularity, best_for, weigth) VALUES (%s, %s, %s, %s, %s)"
    values = (name, year, popularity, best_for, weigth)
    cursor.execute(sql, values)
    db_connection.commit()
  except mysql.connector.Error as err:
    print(f"Something went wrong: {err}")


cursor.close()
