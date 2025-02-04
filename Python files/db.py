import sqlite3

class DBConnect:
	def __init__(self):
		self._db = sqlite3.connect('information.db')
		self._db.row_factory = sqlite3.Row
		self._db.execute('create table if not exists Comp(ID integer primary key autoincrement, Name varchar(255), Gender varchar(255),Phone_No varchar(10),Adhar_No varchar(12), Comment text)')
		self._db.commit()
	def Add(self, name, gender,phone_no,adhar_no,comment):
		self._db.execute('insert into Comp (Name, Gender,Phone_No,Adhar_No,Comment) values (?,?,?,?,?)',(name,gender,phone_no,adhar_no,comment))
		self._db.commit()
		return 'Your complaint has been submitted.'
	def ListRequest(self):
		cursor = self._db.execute('select * from Comp')
		return cursor
