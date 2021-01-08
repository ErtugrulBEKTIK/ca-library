from helpers.dbHelper import connect

class BookModel:

  @connect
  def create(self, cursor, data):

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

    return {'code': 201, 'data': None}

  @connect  
  def getAll(self, cursor):
    sql = ''' SELECT * FROM books '''
    cursor.execute(sql)

    result = cursor.fetchall()
    return {'code': 200, 'data': result}

  @connect
  def getById(self, cursor, bookId):
    sql = ''' SELECT * FROM books WHERE id = %s '''
    cursor.execute(sql, (bookId, ))

    result = cursor.fetchone()

    if(result == None):
      return {'code': 404, 'data': None}

    return {'code': 200, 'data': result}

    