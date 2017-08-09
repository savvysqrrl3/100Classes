class Usersdb(object):
	def __init__(self):
		self.contents = []

	def create(self, name, age):
		# make instance of user object and add to list(return the new object)
		user = {}
		user["name"] = name
		user["age"] = age
		self.contents.append(user)
		return self

	def get(self, name):
		# find and return one user that matches the name and age criterion
		for person in self.contents:
			for userkey in person:
				if person["name"] == name:
				# keyval = person[userkey]
				# # if keyval == name and age:
				# if userkey == "age" and keyval == age:
				# 	if userkey == "name" and keyval == name:
				# 		print person
					print person
					return person

	def filter(self, name):
		# find and return all users with the same name
		temp = []
		for person in self.contents:
			if person["name"] == name:
				temp.append(person)
			# for userkey in person:
			# 	keyval = person[userkey]
			# 	if keyval == name:
			# 		print person
		print temp
		return temp

	def all(self):
		# return all user objects in the list
		print self.contents
		return self

	def exclude(self, name):
		temp = []
		for person in self.contents:
			if person["name"] != name:
				temp.append(person)
		print temp
		return temp



# Instances
database1 = Usersdb()

# Tests/run functions
database1.create("Bob Smith", 50)
database1.create("Mary Smith", 48)
database1.create("Harriet Smith", 10)
database1.create("Eugene Smith", 7)
database1.create("David Jones", 36)
database1.create("Sarah Johnson", 26)
database1.create("Bob Smith", 72)
database1.create("David Jones", 50)

# database1.all()
database1.filter("Bob Smith")
# database1.filter("Mary Smith")
# database1.get("David Jones", 36)
# database1.get("Mary Jones", 23)
# database1.get("Bob Smith")
# database1.get("David Jones")

