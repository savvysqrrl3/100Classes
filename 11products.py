
class Productdb(object):
	def __init__(self):
		self.products = []

	def create(self, name, price, qty):
		prod = {"name":name, "price":price, "qty":qty}
		self.products.append(prod)
		# print self.products
		return self

	def get(self, name):
		for product in self.products:
			if product["name"] == name:
				print product
				return product
		# return self

	def filter(self, name):
		results = []
		for product in self.products:
			if product["name"] == name:
				results.append(product)
		print results
		return results
		# return self

	def exclude(self, name):
		results = []
		for product in self.products:
			if product["name"] != name:
				results.append(product)
		print results
		return results

	def count(self, name):
		sum = 0
		for product in self.products:
			if product["name"] == name:
				sum += 1
		print sum
		return sum

	def total(self, name):
		return self

	def update(self, name, new_qty=None, new_price=None, new_name=None):
		# alternate version:
		# results = self.get(name)
		# if new_name == None:
		# 	pass
		# else: results.name = new_name
		# if new_price == None:
		# 	pass
		# else: results.price = new_price
		# if new_qty == None:
		# 	pass
		# else: results.qty = new_qty
		# return self

		results = {}
		for i in range(0, len(self.products)):
			if self.products[i]["name"] == name:		 
				results = {"name":self.products[i]["name"], "price":self.products[i]["price"], "qty":self.products[i]["qty"]}
				print results

				if new_name == None:
					new_name = results["name"]
				if new_price ==None:
					new_price = results["price"]
				if new_qty == None:
					new_qty = results["qty"]
				print results
		this_one = i
		print this_one
		results["name"] = new_name
		results["price"] = new_price
		results["qty"] = new_qty
		print results
		self.products[this_one] = {"name":results["name"], "price":results["price"], "qty":results["qty"]}
		
		return self

db1 = Productdb()

db1.create("chocolate eclair", 2.50, 2).create("cream puff", 1.75, 1).create("croissant", 0.99, 4).create("cream puff", 1.75, 3).create("brioche", 0.75, 2)

# db1.get("croissant")
# db1.filter("cream puff")
# db1.exclude("cream puff")
# db1.count("cream puff")
db1.update("brioche", 8, 1.05)
print db1.products






