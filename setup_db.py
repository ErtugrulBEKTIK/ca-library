import mysql.connector
from settings import db_settings


setup_sql = '''
CREATE TABLE IF NOT EXISTS roles (
  id int(11) NOT NULL AUTO_INCREMENT, 
  name varchar(255) DEFAULT NULL, 
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS users (
  id int(11) NOT NULL AUTO_INCREMENT, 
  firstName varchar(255) NOT NULL, 
  lastName varchar(255) NOT NULL,
  fullName varchar(255) GENERATED ALWAYS AS
  (concat(coalesce(firstName,''),' ',coalesce(lastName,''))) STORED, 
  email varchar(255) NOT NULL,
  password varchar(255) NOT NULL,
  avatar varchar(255) NOT NULL,
  roleId int(11) DEFAULT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY email (email),
  KEY roleId (roleId),
  CONSTRAINT users_ibfk_1 FOREIGN KEY (roleId) REFERENCES roles (id) ON
  DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS authors (
  id int(11) NOT NULL AUTO_INCREMENT, 
  fullName varchar(255) DEFAULT NULL, 
  description text DEFAULT NULL, 
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS books (
  id int(11) NOT NULL AUTO_INCREMENT, 
  title varchar(255) DEFAULT NULL, 
  description text DEFAULT NULL,
  year year DEFAULT NULL,
  shelf varchar(255) DEFAULT NULL,
  status int(4) DEFAULT 1,
  borrowable tinyint(1) DEFAULT 1,
  publisher varchar(255) DEFAULT NULL, 
  barcode varchar(255) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY barcode (barcode)
);

CREATE TABLE IF NOT EXISTS bookAuthors (
  bookId int(11) NOT NULL,
  authorId int(11) NOT NULL,
  PRIMARY KEY (bookId,authorId),
  KEY authorId (authorId),
  CONSTRAINT bookAuthors_ibfk_1 FOREIGN KEY (bookId) REFERENCES books
  (id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT bookAuthors_ibfk_2 FOREIGN KEY (authorId) REFERENCES authors
  (id) ON DELETE RESTRICT ON UPDATE CASCADE );

CREATE TABLE IF NOT EXISTS categories (
  id int(11) NOT NULL AUTO_INCREMENT, 
  name varchar(255) DEFAULT NULL, 
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS bookCategories (
  bookId int(11) NOT NULL,
  categoryId int(11) NOT NULL,
  PRIMARY KEY (bookId,categoryId),
  KEY categoryId (categoryId),
  CONSTRAINT bookCategories_ibfk_1 FOREIGN KEY (bookId) REFERENCES books
  (id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT bookCategories_ibfk_2 FOREIGN KEY (categoryId) REFERENCES
  categories (id) ON DELETE RESTRICT ON UPDATE CASCADE 
);

CREATE TABLE IF NOT EXISTS bookings (
  id int(11) NOT NULL AUTO_INCREMENT,
  status int(11) DEFAULT 1,
  startDate datetime DEFAULT NULL,
  endDate datetime DEFAULT NULL,
  userId int(11) DEFAULT NULL,
  bookId int(11) DEFAULT NULL,
  PRIMARY KEY (id),
  KEY bookings_bookId_foreign_idx (bookId),
  KEY userId (userId),
  CONSTRAINT bookings_bookId_foreign_idx FOREIGN KEY (bookId) REFERENCES
  books (id) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT bookings_ibfk_1 FOREIGN KEY (userId) REFERENCES users (id)
  ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS comments (
  id int(11) NOT NULL AUTO_INCREMENT,
  content text DEFAULT NULL,
  status tinyint(1) DEFAULT 0,
  star float DEFAULT NULL,
  userId int(11) DEFAULT NULL,
  bookId int(11) DEFAULT NULL,
  createdAt datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id),
  KEY userId (userId),
  KEY bookId (bookId),
  CONSTRAINT comments_ibfk_5 FOREIGN KEY (userId) REFERENCES users (id)
  ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT comments_ibfk_6 FOREIGN KEY (bookId) REFERENCES books (id)
  ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS wishes (
  id int(11) NOT NULL AUTO_INCREMENT,
  notify tinyint(1) DEFAULT NULL,
  createdAt datetime NOT NULL DEFAULT current_timestamp(),
  userId int(11) DEFAULT NULL,
  bookId int(11) DEFAULT NULL,
  PRIMARY KEY (id),
  KEY userId (userId),
  KEY bookId (bookId),
  CONSTRAINT wishes_ibfk_5 FOREIGN KEY (userId) REFERENCES users (id) ON
  DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT wishes_ibfk_6 FOREIGN KEY (bookId) REFERENCES books (id) ON
  DELETE SET NULL ON UPDATE CASCADE
);
'''
connection = mysql.connector.connect(**db_settings, use_pure=True)
cursor = connection.cursor()

results = cursor.execute(setup_sql, multi=True)
for cur in results:
    print('Running:', cur)
   

connection.commit()

cursor.close()
connection.close()
