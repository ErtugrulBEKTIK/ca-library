import mysql.connector as dbapi2
from settings import db_settings

class AuthorModel:

  def create(self, data):

    try:
      connection = dbapi2.connect(**db_settings)
      cursor = connection.cursor()

      # Insert book into db
      sql = '''
      INSERT INTO authors (fullName, description)
      VALUES (%(fullName)s, %(description)s)
      '''
      cursor.execute(sql, data)
     
      connection.commit()

      cursor.close()
    except mysql.DatabaseError:
      connection.rollback()
      return False
    finally:
      connection.close()
      return True
    
  
    
  def getAll(self):
    connection = dbapi2.connect(**db_settings)
    cursor = connection.cursor(dictionary=True)

    sql = '''
    SELECT title, description FROM authors
    '''
    cursor.execute(sql)

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

  def getById(self, id):
    connection = dbapi2.connect(**db_settings)
    cursor = connection.cursor(dictionary=True)

    sql = '''
    SELECT title, description FROM authors WHERE id = 1
    '''
    cursor.execute(sql)

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result

    
    