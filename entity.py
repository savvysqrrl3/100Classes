class Entity(object):
	def __init__(self, name, race, ability, weapon, allegiance, stealth=5, strength=5, damage=0, suspicion=False, trust=True, alive=True, hostage=False):
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
		self.alive = alive
		self.hostage = hostage
		self.prisoners = []

	def defend(self, entity, max_damage):
		# lowers strength of opponent by a small amount (depending on weapon and ability) and inflicts damage, suspicion=True, trust=False
		# if strength of opponent reaches 0, take hostage? If damage of either reaches max, and strength is = 0, alive == False
		# if death condition is reached, print "(name) has died." If another entity tries to attack someone who is dead, print "(name) is already dead, and cannot participate in the fight."
		return self

	