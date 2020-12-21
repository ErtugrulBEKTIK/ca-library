import mysql.connector
from settings import db_settings

def run_create(statement, data = {}):
  try:
    connection = mysql.connector.connect(**db_settings)
    cursor = connection.cursor()


    x = cursor.execute(statement, data)
    print(x)
    connection.commit()

    cursor.close()
  except mysql.DatabaseError:
    connection.rollback()
    return False
  finally:
    connection.close()
    return True

def run_select(statement, one = False):
  try:
    connection = mysql.connector.connect(**db_settings)
    cursor = connection.cursor(dictionary=True)

    cursor.execute(statement)

    if one:
      result = cursor.fetchone()
    else:
      result = cursor.fetchall()

    cursor.close()
  except mysql.DatabaseError:
    connection.rollback()
    return False
  finally:
    connection.close()
    return result


