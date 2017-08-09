
class Bank(object):
	def __init__(self, vault):
		self.members = []
		self.accounts = []
		self.vault = vault
		self.assets = []
		# functions to add members, count accounts by type, add assets, and have a vault

class Member(object):
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.accounts = []
		# functions to add an account, close an account, make payments from one account to another, make transfers

class Account(object):
	def __init__(self, owner, account_type, opening_balance):
		self.owner = owner
		self.account_type = account_type
		self.balance = opening_balance
		
class Checking(Account):
	def __init__(self, account_name):
		self.account_name = account_name
		self.account_type = account_type
		self.balance = opening_balance
# deposit, withdraw, add fee, overdraft 

class Credit(Account):
	def __init__(self, card_name, credit_limit):
		self.card_name = card_name
		self.account_type = account_type
		self.balance = opening_balance
		self.credit = credit_limit
		# functions to charge interest, use credit (make credit go down, and balance go up), make payments

class Savings(Account):
	def __init__(self, account_name)
	self.account_name = account_name
	self.balance = opening_balance
	# functions to make deposit, make withdrawal, and receive interest on total

class HomeLoan(Account):
	def __init__(self, account_name)
	self.account_name = account_name
	self.balance = opening_balance
	# functions to charge interest, make payments


class Vault(object):
	def __init__(self):
		self.cash = {}
		self.coin = {}
		self.valuables = []
		# functions to make deposits and withdrawals, count totals by cash or coin type, total of all
		

class Asset(object):
	def __init__(self, asset_type, worth):
		self.asset_type = asset_type
		self.worth = worth
		# functions for appreciation, depreciation, etc.




	

