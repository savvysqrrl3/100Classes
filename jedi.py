class Jedi(object):
	def __init__(self, name, lightsaber, force_sensitivity, allegiance, stealth=15, strength=25, damage=0, dark=False, suspicion=False, trust=True, alive=True, hostage=False):
		self.name = name
		self.lightsaber = lightsaber
		self.force = force_sensitivity
		self.allegiance = allegiance
		self.suspicion =suspicion
		self.trust = trust
		self.stealth = stealth
		self.strength = strength
		self.damage = damage	
		self.darkness = dark
		self.alive = alive
		self.hostage = hostage
		self.prisoners = []

	def forceLift(self, item, location, height, weight):
		# moves item to a new location, reduces weight value, lifts it to a specified height. Print a statement, then return values to normal?
		return self

	def forcePresence(self, entity, range):
		# detect number of entity objects in range
		return self

	def mindTrick(self, entity):
		# changes entity's suspicion boolean to False, and trust to True, if not already, or vice versa
		return self

	def defend(self, agressor):
		# stealth reduced, reduces agressors strength and increases damage
		return self

	def infiltrate(self, entity):
		# for entities in range, strength is reduced, suspicion is False
		return self









