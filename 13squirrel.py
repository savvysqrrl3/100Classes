

class Squirrel(object):
	def __init__(self, name, fur_color, habitat, tail=True):
		self.name = name
		self.fur_color = fur_color
		self.habitat = habitat
		self.tail = tail



squirrel1 = Squirrel("golden mantled ground squirrel", "golden brown with white and brown stripes", "ground, forest")
squirrel2 = Squirrel("Western gray squirrel", "gray", "trees, forest")
squirrel3 = Squirrel("Douglas squirrel", "dark gray with white belly and brown stripes on sides", "trees, forest")


print squirrel1.name 
print squirrel2.name  
print squirrel3.name