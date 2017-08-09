class Owner(object):
	def __init__(self, name):
		self.name = name
		self.pets = []

	def addPet(self, new_pet):
		# add a pet object to the list of pets
		self.pets.append(new_pet)
		# change pet's owner attribute value to object of person adding pet
		new_pet.owner = self
		print new_pet.name, "has been adopted by", new_pet.owner.name
		return self

	def speak(self, pet_name):
		# make variable for pet's name, and find the name...
		temp = None
		# make for-loop to search all pets in the array for the name that matches
		for critter in self.pets:
			if critter.name == pet_name:
		# assign matching name to variable
				temp = critter
		# call pet's speak function
		print "{} says '{}, speak!'".format(self.name, temp.name)
		print "{} says:".format(temp.name) 
		temp.speak()


class Pet(object):
	def __init__(self, kind, name, response, owner = None):
		self.kind = kind
		self.name = name
		self.response = response
		self.owner = owner

	def speak(self):
		# pass response to caller: owner speak function
		print self.response
		return self

# Instances

pet1 = Pet("dog", "Rover", "Let's go play! ...Treat? ... Squirrel!")
pet2 = Pet("cat", "Fluffy", "Whatever you want, it's less important than what I'm doing. Because I'm a cat.")
pet3 = Pet("bird", "Polly", "Whazzup, yo?")
pet4 = Pet("fish", "Goldie", "bubble bubble... o o o o o O O O")
pet5 = Pet("hamster", "PeeWee", "I'm napping. Touch me and I'll bite your finger off!")
pet6 = Pet("iguana", "Spike", "Takin' it easy duuuuude... Can I hide under the couch and scare your mom?")
pet7 = Pet("python", "Monty", "I love code... when it's my own!")
pet8 = Pet("bobcat", "Taco", "Can I bite you and destroy your house?")
pet9 = Pet("orca", "Willy", "I just want to go hooooooome.... :-(")
pet10 = Pet("dragon", "Viserion", "On my way... Whose ships shall I torch for you today, Mom?")
pet11 = Pet("dragon", "Elliott", "hum hum hum hum....")
pet12 = Pet("dragon", "Toothless", "(((*fireball*))")

owner1 = Owner("Johnny")
owner2 = Owner("Susie")
owner3 = Owner("Dick")
owner4 = Owner("Jane")
owner5 = Owner("Joe")
owner6 = Owner("Ray")
owner7 = Owner("Jesse")
owner8 = Owner("Danaerys")
owner9 = Owner("Pete")
owner10 = Owner("Hiccup")

# Function calls:

# print pet1.kind, pet1.name
# print owner4.name

owner4.addPet(pet3).addPet(pet1)
owner1.addPet(pet6).addPet(pet4)
owner2.addPet(pet2)
owner3.addPet(pet5)
owner5.addPet(pet7)
owner6.addPet(pet8)
owner7.addPet(pet9)
owner8.addPet(pet10)
owner9.addPet(pet11)
owner10.addPet(pet12)

owner4.speak("Polly")
owner4.speak("Rover")
owner1.speak("Spike")
owner1.speak("Goldie")
owner2.speak("Fluffy")
owner3.speak("PeeWee")
owner5.speak("Monty")
owner6.speak("Taco")
owner7.speak("Willy")
owner8.speak("Viserion")
owner9.speak("Elliott")
owner10.speak("Toothless")


