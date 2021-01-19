from helpers.dbHelper import connect
from datetime import datetime, timedelta
from enums import BookingStatus, BookStatus
import json

class BookingModel:

  @connect
  def borrowBook(self, cursor, userId, bookId):
    
    #Check book is available
    sql = 'SELECT * FROM books WHERE status = %s AND borrowable = 1'
    cursor.execute(sql, (BookStatus.AVAILABLE.value,))
    result = cursor.fetchone()

    if(result == None):
      return {'code': 404, 'data': None}


    # Get current date
    startDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    endDate = (datetime.now()+timedelta(weeks=2)).strftime("%Y-%m-%d %H:%M:%S")

    
    # Create booking record
    sql = '''
      INSERT INTO bookings (status, startDate, endDate, userId, bookId)  
      VALUES (%s,%s,%s,%s,%s)
    '''
    cursor.execute(sql, (BookingStatus.BORROWED.value, startDate, endDate, userId, bookId))

   
    # Change book status
    sql = 'UPDATE books SET status = %s WHERE id = %s'
    cursor.execute(sql, (BookStatus.BORROWED.value, bookId))

    # Delete book in wishlist if exist
    sql = 'DELETE FROM wishes WHERE bookId = %s AND userId = %s'
    cursor.execute(sql, (bookId, userId))

    return {'code': 204, 'data': None}

  @connect  
  def getAll(self, cursor, options):

    # Get records by page 
    recordStart = (options.pageNumber - 1) * options.pageSize

    sql = '''SELECT bookings.*, b.title as bookTitle FROM bookings 
      INNER JOIN books as b ON bookings.bookId = b.id
      WHERE userId = %s ORDER BY startDate DESC LIMIT %s, %s 
    '''

    cursor.execute(sql, (options.userId, recordStart, options.pageSize))
    
    bookings = cursor.fetchall()

    # Get total count
    sql = 'SELECT COUNT(*) as count FROM bookings WHERE userId = %s'
    cursor.execute(sql,(options.userId,))
    count = cursor.fetchone()['count']

    # Convert date object to string
    bookings = json.loads(json.dumps(bookings, default=str))

    return {'code': 200, 'data': { 'count': count, 'rows': bookings }}

  @connect
  def returnBook(self, cursor, userId, bookingId):
    
    # Get current date
    returnDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 
    status = BookingStatus.RETURNED.value

    # Change booking status
    sql = ''' UPDATE bookings SET status = %s, endDate = %s
              WHERE id = %s AND userId = %s '''
    
    cursor.execute(sql, (status, returnDate, bookingId, userId))

    # Get book id
    sql = 'SELECT bookId from bookings WHERE id = %s AND userId = %s '
    cursor.execute(sql, (bookingId, userId))
    bookId = cursor.fetchone()['bookId']

    # Change book status
    sql = 'UPDATE books SET status = %s WHERE id = %s'
    cursor.execute(sql, (BookStatus.AVAILABLE.value, bookId))

    return {'code': 204, 'data': None}
