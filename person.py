from car import Car

class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.owns = []

	def getCar(self, make, color):
		# validate whether age is >= 16, else return error
		if self.age >=16:
			print "Approved: age is at least 16 years old."
		else:
			print "Error: must be at least 16 years old to drive a car."
			return False
		# add car object to self.owns list
		self.owns.append(Car(make, color))
		print "Car added"
		return self

	def showCars(self):
		for car in self.owns:
			print car.color, car.make