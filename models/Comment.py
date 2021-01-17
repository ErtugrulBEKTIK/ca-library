from helpers.dbHelper import connect
from datetime import datetime, timedelta
import json

class CommentModel:

  @connect
  def create(self, cursor, options):
    
    # Create comment record
    sql = '''
      INSERT INTO comments (star, content, userId, bookId)  
      VALUES (%(star)s,%(content)s,%(userId)s,%(bookId)s)
    '''
    cursor.execute(sql, options)

    return {'code': 204, 'data': None}


  @connect  
  def getUserComment(self, cursor, options):

    sql = 'SELECT * FROM comments WHERE userId = %s AND bookId = %s'

    cursor.execute(sql, (options.userId, options.bookId))
    comment = cursor.fetchone()

    # Convert date object to string
    comment = json.loads(json.dumps(comment, default=str))

    return {'code': 200, 'data': comment}



  @connect  
  def getBookComments(self, cursor, options):

    # Get records by page 
    recordStart = (options.pageNumber - 1) * options.pageSize

    sql = '''SELECT comments.*, u.fullName as user, u.avatar FROM comments 
      INNER JOIN users as u ON comments.userId = u.id
      WHERE bookId = %s AND status = 1 ORDER BY createdAt DESC LIMIT %s, %s 
    '''

    cursor.execute(sql, (options.bookId, recordStart, options.pageSize))
    
    comments = cursor.fetchall()

    # Get total count
    sql = 'SELECT COUNT(*) as count FROM comments WHERE bookId = %s AND status = 1'
    cursor.execute(sql,(options.bookId,))
    count = cursor.fetchone()['count']

    # Convert date object to string
    comments = json.loads(json.dumps(comments, default=str))

    return {'code': 200, 'data': { 'count': count, 'rows': comments }}

  @connect  
  def getAll(self, cursor, options):

    # Get records by page 
    recordStart = (options.pageNumber - 1) * options.pageSize

    sql = '''SELECT comments.*, u.fullName as user, u.avatar, b.title as book FROM comments 
      INNER JOIN users as u ON comments.userId = u.id
      INNER JOIN books as b ON comments.bookId = b.id
      WHERE comments.status = %s ORDER BY createdAt DESC LIMIT %s, %s 
    '''

    cursor.execute(sql, (options.status, recordStart, options.pageSize))
    
    comments = cursor.fetchall()

    # Get total count
    sql = 'SELECT COUNT(*) as count FROM comments WHERE status = %s'
    cursor.execute(sql,(options.status,))
    count = cursor.fetchone()['count']

    # Convert date object to string
    comments = json.loads(json.dumps(comments, default=str))

    return {'code': 200, 'data': { 'count': count, 'rows': comments }}

  @connect
  def updateByUser(self, cursor, options):
    
    # Create comment record
    sql = '''
      UPDATE comments SET star = %(star)s, content = %(content)s 
      WHERE userId = %(userId)s AND bookId = %(bookId)s
    '''
    cursor.execute(sql, options)

    return {'code': 204, 'data': None}

  @connect
  def approve(self, cursor, commentId):
    
    # Approve comment
    sql = 'UPDATE comments SET status = 1 WHERE id = %s'
    cursor.execute(sql, (commentId,))

    return {'code': 204, 'data': None}

  @connect
  def delete(self, cursor, commentId):
    
    sql = 'DELETE FROM comments WHERE id = %s'
    cursor.execute(sql, (commentId,))

    return {'code': 204, 'data': None}
