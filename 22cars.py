from person import Person
from car import Car

def createValidate(name, age):
	sum = 0
	if type(name) == str:
		print "Validated: name is a string"
	else:
		print "Error: name is not a string"
		return False
	for char in name:
		sum += 1
	if sum >= 3:
		print "Validated: name is at least 3 characters long."	
	else:
		print "Error: name must be at least 3 characters long."
		return False
	if type(age) == int:
		print "Validated: age is an integer."
	else:
		print "Error: age must be an integer."
		return False
	person = Person(name, age)
	print person.name, "created"
	return person



createValidate("Alice", 42).getCar("Toyota", "blue").showCars()
createValidate("Bret", 39).getCar("Porche", "yellow").getCar("Subaru", "green").showCars()
createValidate("Grace", 14).getCar("Honda", "red")
createValidate("Derek", 16).getCar("Ford", "green").showCars()
createValidate("April", 34).getCar("Suzuki", "silver").getCar("Porche", "blue").showCars()
createValidate("Bob", "50")
createValidate(["Fred"], 76)
createValidate("Yi", 37)