import functools
import mysql.connector as dbapi2
from settings import db_settings

def connect(func):
    @functools.wraps(func)
    def wrap(self, *args, **kwargs):
      anyError = False
      try:
        connection = dbapi2.connect(**db_settings)
        cursor = connection.cursor(dictionary=True, buffered=True)

        return func(self, cursor, *args, **kwargs)

      except dbapi2.errors.Error as err:
        anyError = True
        #print(err) 
        raise err
        connection.rollback()

        return {'code': 422, 'data': None}

      except Exception as err:
        anyError = True
        #print(err) 
        raise err
        return {'code': 500, 'data': None}

      finally:
        if not anyError: connection.commit()

        cursor.close() 
        connection.close()
    return wrap
