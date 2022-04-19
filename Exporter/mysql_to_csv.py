import mysql.connector
import pandas as pd


db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="web_scrapping_bgg")
cursor = db_connection.cursor()


def sql_to_csv():
  try:
    query = 'SELECT * FROM bg ORDER BY id'
    results = pd.read_sql_query(query, db_connection)
    results.to_csv("../boardgames.csv", index=False)
  except mysql.connector.Error as err:
    print(f"Something went wrong: {err}")

sql_to_csv()
