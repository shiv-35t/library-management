import mysql.connector

db = mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='1234'
	)

cur = db.cursor()

# cur.execute(f' CREATE DATABASE Librarydb')
# cur.execute(f'USE Library')
# cur.execute(f'CREATE TABLE books ( bookName varchar(300), bookid int PRIMARY KEY, bookAuthor varchar(300), quantity int)')

def addBook(name, id, author, quantity=1):
	cur.execute(f'USE Library')
	cur.execute(f'INSERT INTO books (bookName, bookid, bookAuthor, quantity) values(name, id, author, quantity)')

addBook('Python', 1, 'Sumita Arora')