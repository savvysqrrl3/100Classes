class Set(object):
	def __init__(self):
		self.dragobase = []

	def addDragon(self, dragon):
		self.dragobase.append(dragon)
		return self

	def showAll(self):
		for dragon in self.dragobase:
			print dragon.name
		return self



class Dragon(object):
	def __init__(self, name, kind, color, response, legs=4, wings=True, fire=True):
		self.name = name
		self.kind = kind
		self.color = color
		self.response = response
		self.legs = legs
		self.wings = wings
		self.fire = fire

	def speak(self):
		print self.response
		return self


# Instances
cardSet1 = Set()

dragon1 = Dragon("Elliott", "unknown" "green", "hum hum hum hum", 4)
dragon2 = Dragon("Toothless", "night terror", "black", "chitter chatter")
dragon3 = Dragon("Smaug", "Middle Earth beast", "black", "I like gold...so I'm taking all of yours.")
dragon4 = Dragon("Nameless", "Narnian sea serpent", "multicolored", "You look delicious!", 0, False)
dragon5 = Dragon("Drogon", "Valyrian dragon", "black", "Danaerys is my mom, and I torch enemies for her")
dragon6 = Dragon("Mushu", "Chinese mythical", "red", "Mulan is the man!", 4, True, False)
dragon7 = Dragon("No-name", "two-legged wonder", "purple", "Front legs are overrated.", 2)
dragon8 = Dragon("Viserion", "Valyrian dragon", "gold", "I was named after Danaerys' despicable brother...not sure how I feel about that.")
dragon9 = Dragon("Ice", "Crystal Mountain Camo", "white", "I'm hiding in plain sight on a mountain")
dragon10 = Dragon("Blue Steel", "Runway Special", "steel blue", "The ladies love my signature stare")

 # Function calls

# dragon2.speak()
# print dragon2.legs

cardSet1.addDragon(dragon3).addDragon(dragon8)
cardSet1.showAll()




