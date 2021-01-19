from helpers.dbHelper import connect

class AuthorModel():

  @connect
  def create(self, cursor, data):

    # Insert book into db
    sql = '''
      INSERT INTO authors (fullName, description)
      VALUES (%(fullName)s, %(description)s)
    '''
    cursor.execute(sql, data)
    
  @connect
  def getAll(self, cursor, options):

    # Get records by page 
    if options.pageNumber:
      recordStart = (options.pageNumber - 1) * options.pageSize

    if options.search:
      sql = '''
        SELECT * FROM authors WHERE fullname LIKE %s ORDER BY fullName ASC
      '''
      cursor.execute(sql, ('%'+options.search+'%',))
    else:
      sql = '''
        SELECT id, fullName, description FROM authors ORDER BY fullName ASC LIMIT %s, %s
      '''
      cursor.execute(sql, (recordStart, options.pageSize))
    
    rows = cursor.fetchall()

    # Get total count
    sql = '''
      SELECT COUNT(*) as count FROM authors
    '''
    cursor.execute(sql)
    count = cursor.fetchone()['count']

    return {'code': 200, 'data': { 'count': count, 'rows': rows }}

  @connect
  def getById(self, cursor, id):
    
    sql = '''
      SELECT fullName, description FROM authors WHERE id = %s
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
      UPDATE authors SET fullName = %(fullName)s, description = %(description)s
      WHERE id = %(id)s
    '''
    cursor.execute(sql, data)

    return {'code': 204, 'data': None}

  @connect
  def delete(self, cursor, id):
    sql = 'DELETE FROM authors WHERE id = %s'
    cursor.execute(sql, (id, ))

    return {'code': 204, 'data': None}
