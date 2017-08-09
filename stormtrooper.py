class StormTrooper(object):
	def __init__(self, name, weapon, allegiance, stealth=3, strength=10, damage=0, suspicion=False, trust=True, alive=True, hostage=False):
		self.name = name
		self.weapon = weapon
		self.allegiance = allegiance
		self.stealth = stealth
		self.strength = strength
		self.damage = damage
		self.suspicion =suspicion
		self.trust = trust
		self.alive = alive
		self.hostage = hostage
		self.prisoners = []

	def guard(self, entity):
		# lowers stealth of opponent and lowers strength according to number of ST objects in "pack"
		# Suspicion = True, Trust = False toward all objects of opposing allegiance
		return self

	def attack(self, opponent):
		# inflicts damage on opponent in correlation with number of ST objects in pack
		# stealth of self is reduced to zero, increases damage and reduces strength of opponent
		return self