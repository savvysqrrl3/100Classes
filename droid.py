class Droid(object):
	def __init__(self, kind, name, ability, allegiance, damage=0, functional=True, hostage=False):
		self.kind = kind
		self.name = name
		self.ability = ability
		self.allegiance = allegiance
		self.damage = damage
		self.functional = functional
		self.hostage = hostage

	# create function or condition in which droid is no longer functional (=False) if damage reaches a set amount
	# if damage is minimal or strength is significantly less than opponent, hostage condition is met. 
	# if hostage, add to opponent list and delete from current ship's list (or add to a list belonging to that entity)

