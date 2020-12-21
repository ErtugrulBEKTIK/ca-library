import mysql.connector as dbapi2
from settings import db_settings

class UserModel:

  def create(self, data):

    try:
      connection = dbapi2.connect(**db_settings)
      cursor = connection.cursor()

      # Insert book into db
      sql = '''
        INSERT INTO users (firstName, lastName, email, password, roleId)
        VALUES (%(firstName)s, %(lastName)s, %(email)s, %(password)s, %(roleId)s)
      '''
      cursor.execute(sql, data)
      
      connection.commit()

      return {'code': 201, 'data': None}
     
    except dbapi2.errors.Error:
      connection.rollback()
      return {'code': 422, 'data': None}

    finally:
      cursor.close() 
      connection.close()
      
  def getAll(self):
    try:
      connection = dbapi2.connect(**db_settings)
      cursor = connection.cursor(dictionary=True)

      sql = ''' SELECT * FROM books '''
      cursor.execute(sql)

      result = cursor.fetchall()
      return {'code': 200, 'data': result}

    except dbapi2.errors.Error:
      connection.rollback()
      return {'code': 422, 'data': None}
    finally:
      cursor.close()
      connection.close()

  def getById(self, bookId):
    try:
      connection = dbapi2.connect(**db_settings)
      cursor = connection.cursor(dictionary=True)

      sql = ''' SELECT * FROM books WHERE id = %s '''
      cursor.execute(sql, (bookId, ))

      result = cursor.fetchone()
  
      if(result == None):
        return {'code': 404, 'data': None}

      return {'code': 200, 'data': result}
    
    except dbapi2.errors.Error:
      connection.rollback()
      return {'code': 422, 'data': None}
    finally:
      cursor.close()
      connection.close()

    