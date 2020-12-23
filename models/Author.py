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
    
  
    
  def getAll(self, options):
    connection = dbapi2.connect(**db_settings)
    cursor = connection.cursor(dictionary=True)

    # Get records by page 
    recordStart = (options.pageNumber - 1) * options.pageSize
    sql = '''
      SELECT * FROM authors ORDER BY fullName ASC LIMIT %s, %s
    '''
    cursor.execute(sql, (recordStart, options.pageSize))
    rows = cursor.fetchall()

    # Get total count
    sql = '''
      SELECT COUNT(*) as count FROM authors
    '''
    cursor.execute(sql)
    count = cursor.fetchone()['count']

    cursor.close()
    connection.close()

    return { 'count': count, 'rows': rows }

  def getById(self, id):
    
    try:
      connection = dbapi2.connect(**db_settings)
      cursor = connection.cursor(dictionary=True)

      sql = '''
        SELECT fullName, description FROM authors WHERE id = %s
      '''
      cursor.execute(sql, (id, ))

      result = cursor.fetchone()

      if(result):
        return {'code': 200, 'data': result}
      else:
        return {'code': 404, 'data': None}
     
    except dbapi2.errors.Error:
      connection.rollback()
      return {'code': 422, 'data': None}

    finally:
      cursor.close() 
      connection.close()

  def updateById(self, id, data):
    
    try:
      connection = dbapi2.connect(**db_settings)
      cursor = connection.cursor(dictionary=True)

      data['id'] = id

      print(data)

      sql = '''
        UPDATE authors SET fullName = %(fullName)s, description = %(description)s
        WHERE id = %(id)s
      '''
      cursor.execute(sql, data)

      connection.commit()

      return {'code': 204, 'data': None}
     
    except dbapi2.errors.Error:
      connection.rollback()
      return {'code': 422, 'data': None}

    finally:
      cursor.close() 
      connection.close()

  def delete(self, id):

    try:
      connection = dbapi2.connect(**db_settings)
      cursor = connection.cursor(dictionary=True)

      sql = '''
        DELETE FROM authors WHERE id = %s
      '''
      cursor.execute(sql, (id, ))
      connection.commit()

      return {'code': 204, 'data': None}
     
    except dbapi2.errors.Error:
      connection.rollback()
      return {'code': 422, 'data': None}

    finally:
      cursor.close() 
      connection.close()
    