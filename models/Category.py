from helpers.dbHelper import connect

class CategoryModel():

  @connect
  def create(self, cursor, data):

    # Insert book into db
    sql = '''
      INSERT INTO categories (name)
      VALUES (%(name)s)
    '''
    cursor.execute(sql, data)
    
  @connect
  def getPaginated(self, cursor, options):

    # Get records by page 
    if options.pageNumber:
      recordStart = (options.pageNumber - 1) * options.pageSize

    if options.search:
      sql = 'SELECT * FROM categories WHERE name LIKE %s ORDER BY name ASC'
      cursor.execute(sql, ('%'+options.search+'%',))
    else:
      sql = 'SELECT * FROM categories ORDER BY name ASC LIMIT %s, %s'
      cursor.execute(sql, (recordStart, options.pageSize))

    rows = cursor.fetchall()

    # Get total count
    sql = '''
      SELECT COUNT(*) as count FROM categories
    '''
    cursor.execute(sql)
    count = cursor.fetchone()['count']

    return {'code': 200, 'data': { 'count': count, 'rows': rows }}


  @connect
  def getAll(self, cursor):

    
    cursor.execute('SELECT * FROM categories ORDER BY name')
    categories = cursor.fetchall()

    return {'code': 200, 'data': categories}


  @connect
  def getById(self, cursor, id):
    
    sql = '''
      SELECT name FROM categories WHERE id = %s
    '''
    cursor.execute(sql, (id, ))

    result = cursor.fetchone()

    if(result):
      return {'code': 200, 'data': result}
    else:
      return {'code': 404, 'data': None}

  @connect
  def updateById(self, cursor, id, data):
    
    data['id'] = id
    sql = '''
      UPDATE categories SET name = %(name)s
      WHERE id = %(id)s
    '''
    cursor.execute(sql, data)

    return {'code': 204, 'data': None}

  @connect
  def delete(self, cursor, id):
    sql = '''
      DELETE FROM categories WHERE id = %s
    '''
    cursor.execute(sql, (id, ))

    return {'code': 204, 'data': None}
