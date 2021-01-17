from helpers.dbHelper import connect
from datetime import datetime, timedelta
from enums import BookStatus
import json

class WishModel:

  @connect
  def create(self, cursor, userId, bookId):
    
    # Create wish record
    sql = '''
      INSERT INTO wishes (notify, userId, bookId)  
      VALUES (%s,%s,%s)
    '''
    cursor.execute(sql, (1, userId, bookId))

    return {'code': 204, 'data': None}

  @connect  
  def getAll(self, cursor, options):

    # Get records by page 
    recordStart = (options.pageNumber - 1) * options.pageSize

    sql = '''SELECT wishes.*, b.title as bookTitle, b.status FROM wishes 
      INNER JOIN books as b ON wishes.bookId = b.id
      WHERE userId = %s ORDER BY id DESC LIMIT %s, %s 
    '''

    cursor.execute(sql, (options.userId, recordStart, options.pageSize))
    
    wishes = cursor.fetchall()

    # Get total count
    sql = 'SELECT COUNT(*) as count FROM wishes WHERE userId = %s'
    cursor.execute(sql,(options.userId,))
    count = cursor.fetchone()['count']

    # Convert date object to string
    wishes = json.loads(json.dumps(wishes, default=str))

    return {'code': 200, 'data': { 'count': count, 'rows': wishes }}

  @connect  
  def notifications(self, cursor, userId):

    sql = '''SELECT wishes.*, b.title as bookTitle, b.status FROM wishes 
      INNER JOIN books as b ON wishes.bookId = b.id
      WHERE userId = %s AND b.status = %s ORDER BY id DESC
    '''

    cursor.execute(sql, (userId, BookStatus.AVAILABLE.value))
    
    notifications = cursor.fetchall()

    # Convert date object to string
    notifications = json.loads(json.dumps(notifications, default=str))

    return {'code': 200, 'data': notifications}

  @connect
  def delete(self, cursor, userId, wishId):
    
    # We check also userId to sure the user remove own wish
    sql = 'DELETE FROM wishes WHERE userId = %s AND id = %s'
    cursor.execute(sql, (userId, wishId))

    return {'code': 204, 'data': None}
