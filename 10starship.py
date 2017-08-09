from jedi import Jedi
from stormtrooper import StormTrooper
from entity import Entity
from droid import Droid

class StarShip(object):
	def __init__(self, name, classification, shields, weapons, strength, damage=0, boarded=False):
		self.name = name
		self.classification = classification
		self.shields = shields
		self.weapons = weapons
		self.strength = strength
		self.damage = damage
		self.boarded = boarded
		self.passengers = []

	def addPassengers(self, new_entity):
		# add jedi, stormtroopers, droids, and other entities
		self.passengers.append(new_entity)
		print new_entity.name or new_entity.kind, "is now on board the ",self.name
		return self

	def manifest(self):
		# show all passengers aboard
		for passenger in self.passengers:
			print passenger.name or passenger.kind
		return self

	def battle(self):
		# if there are objects with opposing allegiance on board, have them fight each other... Use random to determine who fights whom?
		# print name vs. name, weapons, strength, and damage.
		# when victory condition or death condition is reached, print results (strength, damage, who won/died).
		# hostage situation?
		# if death condition is reached, print message and then delete object from the passenger list.
		return self

	def shipBattle(self)
		# initiate a battle between ship objects.
		return self

# Instances
ship1 = StarShip("Millenium Falcon", "cargo vessel", 10, 15, 20)
ship2 = StarShip("Sigma", "Star Destroyer", 20, 50, 100)

Leia = Entity("Princess Leia", "human", "diplomacy", "blaster", "Rebellion", 9, 8)
Han = Entity("Han Solo", "human", "smuggling", "blaster", "Rebellion", 4, 10)
C3PO = Droid("translator droid", "C3PO", "language translation", "Rebellion")
R2D2 = Droid("astromech droid", "R2D2", "computer communications", "Rebellion")
Chewie = Entity("Chewbacca", "wookie", "copilot", "crossbow", "Rebellion", 3, 15)
Luke = Jedi("Luke Skywalker", "Blue", 8, "Rebellion", 12, 18)

STa = StormTrooper("stormtrooper a", "blaster", "Empire")
STb = StormTrooper("stormtrooper b", "blaster", "Empire")
STc = StormTrooper("stormtrooper c", "blaster", "Empire")
STd = StormTrooper("stormtrooper d", "blaster", "Empire")
STe = StormTrooper("stormtrooper e", "blaster", "Empire")
Vader = Jedi("Darth Vader", "Red", 18, "Empire", 11, 22, 0, True)
S122B = Droid("imperial probe droid", "S122B", "espionage and recon", "Empire")



# Function calls
# print ship1.name
# print ship2.classification

ship1.addPassengers(Leia).addPassengers(Han).addPassengers(Chewie).addPassengers(C3PO).addPassengers(R2D2).addPassengers(Luke)
ship1.manifest()

ship2.addPassengers()



