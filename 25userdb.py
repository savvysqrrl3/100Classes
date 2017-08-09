from user import User 

class Userdb(object):
	def __init__(self):
		self.cur_id = 1
		self.users = []

	def create(self, name, age):
		self.users.append(User(name, age, self.cur_id, self))
		self.cur_id += 1
		return self

	def all(self):
		for user in self.users:
			print user.name, user.age
		return self.users

	def get(self, name):
		for user in self.users:
			if user.name == name:
				print user.name, "has been found"
				return user
		print name, "was not found"
		return self

	def filter(self, name):
		match = []
		for user in self.users:
			if user.name == name:
				match.append(user)
		print match
		return match



	def exclude(self, name):
		nonmatch = []
		for user in self.users:
			if user.name != name:
				nonmatch.append(user)
		print nonmatch
		return nonmatch
		return self

	def delete(self, name):
		for user in self.users:
			if user.name == name:
				self.users.remove(user)
				return self
		return self


db1 = Userdb().create("Bob", 50).create("Shirley", 82).create("Amanda", 22).create("Amanda", 44)
print db1.all()
db1.delete("Frank").delete("Amanda")
print db1.all()

db1.get("Shirley")
db1.get("Frank")

db1.filter("Amanda")
db1.exclude("Bob")


