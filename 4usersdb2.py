class Usersdb(object):
	def __init__(self):
		self.users = []

	def create(self, first_name, last_name, age):
		user = {}
		user["first name"] = first_name
		user["last name"] = last_name
		user["age"] = age
		self.users.append(user)
		return user

	def all(self):
		print self.users
		return self.users

	def get(self, first_name, last_name):
		for person in self.users:
			for mykey in person:
				myval = person[mykey]
				if myval == first_name and last_name:
					print person
					
		return self

	def filterbyFirst(self, first_name):
		for person in self.users:
			for mykey in person:
				myval = person[mykey]
				if mykey == "first name" and myval == first_name:
					print person
		return self

	def filterbyLast(self, last_name):
		for person in self.users:
			for mykey in person:
				myval = person[mykey]
				if mykey == "last name" and myval == last_name:
					print person
		return self

	def filterbyAny(self, any_name):
		for person in self.users:
			for mykey in person:
				myval = person[mykey]
				if myval == any_name:
					print person
		return self

	def filterbyAge(self, age):
		for person in self.users:
			for mykey in person:
				myval = person[mykey]
				if myval == age:
					print person
		return self

# Instances
database2 = Usersdb()

# Tests/run functions
database2.create("Bob", "Smith", 50)
database2.create("Mary", "Smith", 50)
database2.create("Harriet", "Smith", 10)
database2.create("Eugene", "Smith", 7)
database2.create("David", "Jones", 36)
database2.create("Sarah", "Johnson", 36)
database2.create("Bob", "Smith", 72)
database2.create("Mary", "James", 50)


# database2.all()
# database2.get("Sarah", "Johnson")
#database2.filterbyFirst("Mary")
# database2.filterbyLast("Smith")
database2.filterbyAny("Mary")
database2.filterbyAny("Smith")
# database2.filterbyAny("David")
# database2.filterbyAge(36)
# database2.filterbyAny("Smith").filterbyAge(50)
# database2.filterbyAge(50).filterbyFirst("Mary")


