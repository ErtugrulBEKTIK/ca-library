from helpers.dbHelper import connect

class BookModel:

  @connect
  def create(self, cursor, data):

    authors = data['authors']
    del data['authors']

    categories = data['categories']
    del data['categories']

    # Set year attr none if empty
    if not data['year']: data['year'] = None

    # Insert book into db
    sql = '''
      INSERT INTO books (title, publisher, year, shelf, barcode, description)
      VALUES (%(title)s, %(publisher)s, %(year)s, %(shelf)s, %(barcode)s, %(description)s)
    '''
    cursor.execute(sql, data)

    bookId = cursor.lastrowid
  
    # Set authors
    for author in authors:
      # Set author id. Insert author if not exist
      if('id' in author): 
        authorId = author['id']
      else:
        sql = ''' INSERT INTO authors (fullName) VALUES (%s) '''
        cursor.execute(sql, (author['fullName'],))
        authorId = cursor.lastrowid

      # Create relation between book and author
      sql = ''' INSERT INTO bookAuthors (bookId, authorId) VALUES (%s, %s) '''
      cursor.execute(sql, (bookId, authorId))

    # Set authors
    for category in categories:
      # Set category id. Insert category if not exist
      if('id' in category): 
        categoryId = category['id']
      else:
        sql = ''' INSERT INTO categories (name) VALUES (%s) '''
        cursor.execute(sql, (category['name'],))
        categoryId = cursor.lastrowid

      # Create relation between book and category
      sql = ''' INSERT INTO bookCategories (bookId, categoryId) VALUES (%s, %s) '''
      cursor.execute(sql, (bookId, categoryId))
    
    return {'code': 201, 'data': None}

  @connect  
  def getAll(self, cursor, options):
     # Get records by page 
    if options.pageNumber:
      recordStart = (options.pageNumber - 1) * options.pageSize

    if options.search:
      sql = '''
        SELECT * FROM books WHERE title LIKE %s ORDER BY title ASC
      '''
      cursor.execute(sql, ('%'+options.search+'%',))
    else:
      sql = '''
        SELECT * FROM books ORDER BY title ASC LIMIT %s, %s
      '''
      cursor.execute(sql, (recordStart, options.pageSize))
    
    rows = cursor.fetchall()

    # Get total count
    sql = 'SELECT COUNT(*) as count FROM books'
    cursor.execute(sql)
    count = cursor.fetchone()['count']

    return {'code': 200, 'data': { 'count': count, 'rows': rows }}

  @connect
  def getById(self, cursor, bookId):
    sql = ''' SELECT * FROM books WHERE id = %s '''
    cursor.execute(sql, (bookId, ))

    result = cursor.fetchone()

    if(result == None):
      return {'code': 404, 'data': None}

    return {'code': 200, 'data': result}

    
  @connect
  def delete(self, cursor, id):
    sql = 'DELETE FROM books WHERE id = %s'
    cursor.execute(sql, (id, ))

    return {'code': 204, 'data': None}