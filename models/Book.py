import mysql.connector as dbapi2
from settings import db_settings

class BookModel:

  def create(self, data):

    try:
      connection = dbapi2.connect(**db_settings)
      cursor = connection.cursor()

      # Insert book into db
      sql = '''
        INSERT INTO books (title, description, year, publisher)
        VALUES (%(title)s, %(description)s, %(year)s, %(publisher)s)
      '''
      cursor.execute(sql, data)

      bookId = cursor.lastrowid

      sql = '''
        INSERT INTO bookAuthors (bookId, authorId)
        VALUES (%s, %s)
      '''
      cursor.execute(sql, (bookId, data['authorId']))
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

    