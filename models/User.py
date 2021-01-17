from helpers.dbHelper import connect
from enums import UserType
from passlib.hash import sha256_crypt

class UserModel:

  @connect
  def create(self, cursor, data):

    data['password'] = sha256_crypt.encrypt(data['password'])

    # Insert book into db
    sql = '''
      INSERT INTO users (firstName, lastName, email, password, roleId)
      VALUES (%(firstName)s, %(lastName)s, %(email)s, %(password)s, %(roleId)s)
    '''
    cursor.execute(sql, data)
    
    userId = cursor.lastrowid

    return {'code': 201, 'data': {'userId': userId}}

  @connect 
  def getAdmins(self, cursor):
    sql = '''SELECT users.id, fullName, firstName, lastName, email, r.name as role FROM users 
      INNER JOIN roles as r ON users.roleId = r.id
      WHERE roleId != %s'''
    cursor.execute(sql, (UserType.BASIC_USER.value,))

    result = cursor.fetchall()
    return {'code': 200, 'data': result}

  @connect  
  def getBasicUsers(self, cursor, options):

    # Get records by page 
    recordStart = (options.pageNumber - 1) * options.pageSize

    sql = '''SELECT users.id, fullName, firstName, lastName, email, r.name as role FROM users 
      INNER JOIN roles as r ON users.roleId = r.id
      WHERE roleId = %s ORDER BY fullName ASC LIMIT %s, %s 
    '''
    cursor.execute(sql, (UserType.BASIC_USER.value, recordStart, options.pageSize))
    
    users = cursor.fetchall()

    # Get total count
    sql = 'SELECT COUNT(*) as count FROM users WHERE roleId = %s'
    cursor.execute(sql,(UserType.BASIC_USER.value,))
    count = cursor.fetchone()['count']

    return {'code': 200, 'data': { 'count': count, 'rows': users }}


  @connect 
  def getById(self, cursor, userId):
    sql = 'SELECT id, fullName, firstName, lastName, email, roleId FROM users WHERE id = %s'
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

  @connect
  def updateById(self, cursor, id, data):
    
    data['id'] = id 
    sql = '''
      UPDATE users SET firstName = %(firstName)s, lastName = %(lastName)s,  
      email = %(email)s, avatar = %(avatar)s WHERE id = %(id)s
    '''
    cursor.execute(sql, data)

    return {'code': 204, 'data': None}

  @connect
  def updateByAdmin(self, cursor, id, data):
    
    data['id'] = id 
    sql = '''
      UPDATE users SET firstName = %(firstName)s, lastName = %(lastName)s,  
      email = %(email)s, roleId = %(roleId)s WHERE id = %(id)s
    '''
    cursor.execute(sql, data)

    return {'code': 204, 'data': None}

  @connect
  def updatePassword(self, cursor, id, password):
  
    sql = 'UPDATE users SET password = %s WHERE id = %s'
    cursor.execute(sql, (password, id))

    return {'code': 204, 'data': None}

  @connect
  def delete(self, cursor, id):
    sql = 'DELETE FROM users WHERE id = %s'
    cursor.execute(sql, (id, ))

    return {'code': 204, 'data': None}
