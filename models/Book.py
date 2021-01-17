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
        sql = 'INSERT INTO authors (fullName) VALUES (%s)'
        cursor.execute(sql, (author['fullName'],))
        authorId = cursor.lastrowid

      # Create relation between book and author
      sql = 'INSERT INTO bookAuthors (bookId, authorId) VALUES (%s, %s)'
      cursor.execute(sql, (bookId, authorId))

    # Set authors
    for category in categories:
      # Set category id. Insert category if not exist
      if('id' in category): 
        categoryId = category['id']
      else:
        sql = 'INSERT INTO categories (name) VALUES (%s)'
        cursor.execute(sql, (category['name'],))
        categoryId = cursor.lastrowid

      # Create relation between book and category
      sql = 'INSERT INTO bookCategories (bookId, categoryId) VALUES (%s, %s)'
      cursor.execute(sql, (bookId, categoryId))
    
    return {'code': 201, 'data': None}

  @connect  
  def getAll(self, cursor, options):
  
    # Get records by page 
    recordStart = (options.pageNumber - 1) * options.pageSize

    searchSql = '%'+options.search+'%' if options.search else '%%';

    # Prepare category SQL
    categoriesSql = ''
    if 'categories' in options and options['categories']:
      tmpArr = []
      for cId in options['categories']:
        tmpArr.append('j.categoryId = {}'.format(cId))

      joined = ' OR '.join(tmpArr)

      categoriesSql = 'AND('+joined+')'

    sql = '''SELECT books.* FROM books 
      RIGHT JOIN bookCategories as j ON j.bookId = books.id
      WHERE title LIKE %s''' + categoriesSql + '''
      GROUP BY id ORDER BY title ASC LIMIT %s, %s 
    '''

    #sql = 'SELECT * FROM books WHERE title LIKE %s ORDER BY title ASC LIMIT %s, %s'
    cursor.execute(sql, (searchSql, recordStart, options.pageSize))
    
    books = cursor.fetchall()

    for book in books:

      # Add authors of book
      sql = '''
        SELECT authors.id, authors.fullName FROM bookAuthors 
        INNER JOIN authors ON bookAuthors.authorId=authors.id
        WHERE bookId = %s
      '''
      cursor.execute(sql, (book['id'],))
      book['authors'] = cursor.fetchall()

      # Add categories of book
      sql = '''
        SELECT categories.id, categories.name FROM bookCategories
        INNER JOIN categories ON bookCategories.categoryId=categories.id
        WHERE bookId = %s
      '''
      cursor.execute(sql, (book['id'],))
      book['categories'] = cursor.fetchall()

      # Add categories of book
      sql = '''
        SELECT COUNT(*) as count, AVG(star) as rating FROM comments
        WHERE bookId = %s AND status = 1
      '''
      cursor.execute(sql, (book['id'],))
      book['comment'] = cursor.fetchone()

    # Get total count
    sql = 'SELECT COUNT(*) as count FROM books WHERE title LIKE %s'
    cursor.execute(sql,(searchSql,))
    count = cursor.fetchone()['count']

    return {'code': 200, 'data': { 'count': count, 'rows': books }}

  @connect  
  def search(self, cursor, search):
    
    sql = 'SELECT * FROM books WHERE title LIKE %s ORDER BY title ASC'
    cursor.execute(sql, ('%'+search+'%',))
    
    rows = cursor.fetchall()

    return {'code': 200, 'data': { 'count': count, 'rows': rows }}


  @connect
  def getById(self, cursor, bookId):
    sql = 'SELECT * FROM books WHERE id = %s'
    cursor.execute(sql, (bookId, ))
    
    book = cursor.fetchone()

    # Add authors of book
    sql = '''
      SELECT authors.id, authors.fullName FROM bookAuthors 
      INNER JOIN authors ON bookAuthors.authorId=authors.id
      WHERE bookId = %s
    '''
    cursor.execute(sql, (book['id'],))
    book['authors'] = cursor.fetchall()

    # Add categories of book
    sql = '''
      SELECT categories.id, categories.name FROM bookCategories
      INNER JOIN categories ON bookCategories.categoryId=categories.id
      WHERE bookId = %s
    '''
    cursor.execute(sql, (book['id'],))
    book['categories'] = cursor.fetchall()

    if(book == None):
      return {'code': 404, 'data': None}

    return {'code': 200, 'data': book}

    
  @connect
  def updateById(self, cursor, bookId, data):

    authors = data['authors']
    del data['authors']

    categories = data['categories']
    del data['categories']

    # Set year attr none if empty
    if not data['year']: data['year'] = None

    data['id'] = bookId

    # Insert book into db
    sql = '''
      UPDATE books SET title=%(title)s, publisher=%(publisher)s, 
      year=%(year)s, shelf=%(shelf)s, barcode=%(barcode)s, description=%(description)s
      WHERE id=%(id)s
    '''
    cursor.execute(sql, data)
  
    ###### REMOVE OLD RELATIONS #######
    # Remove old authors
    cursor.execute('DELETE FROM bookAuthors WHERE bookId = %s', (bookId,))

    #Remove old categories
    cursor.execute('DELETE FROM bookCategories WHERE bookId = %s', (bookId,))

    # Set authors
    for author in authors:
      # Set author id. Insert author if not exist
      if('id' in author): 
        authorId = author['id']
      else:
        sql = 'INSERT INTO authors (fullName) VALUES (%s)'
        cursor.execute(sql, (author['fullName'],))
        authorId = cursor.lastrowid

      # Create relation between book and author
      sql = 'INSERT INTO bookAuthors (bookId, authorId) VALUES (%s, %s)'
      cursor.execute(sql, (bookId, authorId))

    # Set authors
    for category in categories:
      # Set category id. Insert category if not exist
      if('id' in category): 
        categoryId = category['id']
      else:
        sql = 'INSERT INTO categories (name) VALUES (%s)'
        cursor.execute(sql, (category['name'],))
        categoryId = cursor.lastrowid

      # Create relation between book and category
      sql = 'INSERT INTO bookCategories (bookId, categoryId) VALUES (%s, %s)'
      cursor.execute(sql, (bookId, categoryId))
    
    return {'code': 201, 'data': None}


  @connect
  def delete(self, cursor, id):
    sql = 'DELETE FROM books WHERE id = %s'
    cursor.execute(sql, (id, ))

    return {'code': 204, 'data': None}