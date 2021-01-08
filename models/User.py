from helpers.dbHelper import connect

class UserModel:

  @connect
  def create(self, cursor, data):
    # Insert book into db
    sql = '''
      INSERT INTO users (firstName, lastName, email, password, roleId)
      VALUES (%(firstName)s, %(lastName)s, %(email)s, %(password)s, %(roleId)s)
    '''
    cursor.execute(sql, data)
    
    userId = cursor.lastrowid

    return {'code': 201, 'data': {'userId': userId}}

  @connect 
  def getAll(self, cursor):
    sql = ''' SELECT * FROM books '''
    cursor.execute(sql)

    result = cursor.fetchall()
    return {'code': 200, 'data': result}

  @connect 
  def getById(self, cursor, userId):
    sql = ''' SELECT * FROM users WHERE id = %s '''
    cursor.execute(sql, (userId, ))

    result = cursor.fetchone()

    if(result == None):
      return {'code': 404, 'data': None}

    return {'code': 200, 'data': result}

  @connect 
  def getByEmail(self, cursor, email):
    sql = ''' SELECT * FROM users WHERE email = %s '''
    cursor.execute(sql, (email, ))

    result = cursor.fetchone()

    if(result == None):
      return {'code': 404, 'data': None}

    return {'code': 200, 'data': result}