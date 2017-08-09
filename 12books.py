from pprint import pprint

class Booksdb(object):
	def __init__(self):
		self.contents = []
		self.cur_id = 1

	def get_cur_id(self):
		temp = self.cur_id
		self.cur_id += 1
		return temp

	def create(self, title, author):
		self.contents.append(Book(title, author))
		return self

	def showAll(self):
		for book in self.contents:
			print book.title, book.id

	def get(self, id):
		for book in self.contents:
			if book.id == id:
				print book.id, book.title
				return book
		
	def delete(self, id):
		for book in self.contents:
			if book.id == id:
				self.contents.remove(book)

	def filter(self, title):
		for book in self.contents:
			if book.title == title:
				print "found", book.title, book.id
				return book
	
	def exclude(self, title):
		for book in self.contents:
			if book.title != title:
				print book.title
		return book
	


class Book(object):
	def __init__(self, title, author):
		self.title = title
		self.author = author
		self.id = bookbucket1.get_cur_id()


bookbucket1 = Booksdb()

bookbucket1.create("Island of the Blue Dolphins", "Scott O'Dell").create("Call it Courage", "Scott O'Dell").create("East", "Edit Pattou")

# # print bookbucket1.contents
# bookbucket1.showAll()

# bookbucket1.get(2)
# bookbucket1.delete(3)
bookbucket1.showAll()

# bookbucket1.filter("East")
# bookbucket1.exclude("East")


