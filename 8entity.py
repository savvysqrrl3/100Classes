class Entity(object):
	def __init__(self, name, race, ability, weapon, allegiance, stealth=5, strength=5, damage=0, suspicion=False, trust=True):
		self.name = name
		self.race = race
		self.ability = ability
		self.weapon = weapon
		self.allegiance = allegiance
		self.stealth = stealth
		self.strength = strength
		self.damage = damage
		self.suspicion =suspicion
		self.trust = trust
		

	def defend(self, entity):
		# lowers strength of opponent by a small amount (depending on weapon and ability) and inflicts damage, suspicion=True, trust=False
		return self

	