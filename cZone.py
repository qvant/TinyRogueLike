import random

class Zone:
	def __init__(self, world):
		self.type = int(random.random() * 4)
		self.world = world
		if self.type == 0:
			self.descr = "You engaged monster\n"
			self.monster_type = int(random.random() * 4)
			if self.monster_type == 0:
				self.descr += "you see a goblin"
				self.health = 30
				self.attack = 10
				self.defence = 0
				self.gold = 10
				self.exp = 20
			elif self.monster_type == 1:
				self.descr += "you see a ork"
				self.health = 60
				self.attack = 15
				self.defence = 1
				self.gold = 20
				self.exp = 30
			elif self.monster_type == 2:
				self.descr += "you see a black knight"
				self.health = 100
				self.attack = 20
				self.defence = 3
				self.gold = 100
				self.exp = 90
			elif self.monster_type == 3:
				self.descr += "you see a troll"
				self.health = 80
				self.attack = 10
				self.defence = 1
				self.gold = 30
				self.exp = 40
			elif self.monster_type == 4:
				self.descr += "you see a spider"
				self.health = 40
				self.attack = 5
				self.defence = 0
				self.gold = 10
				self.exp = 20
			elif self.monster_type == 5:
				self.descr += "you see a wolf"
				self.health = 50
				self.attack = 10
				self.defence = 2
				self.gold = 20
				self.exp = 40
			self.hint = "Press a to attack, f to flee, h to drink health potion"
			if world > 4:
				self.health = int(self.health * 1.5)
			if world > 2:
				self.defence += self.defence * 2
			if world > 6:
				self.attack = int(self.attack * 1.5)
		elif self.type == 1:
			self.descr = "You see a tavern. Here you can rest for 5 GP"
			self.hint = "Press a to go forward, r to rest"
		elif self.type == 2:
			self.descr = "You see a shop"
			self.hint = "Press a to go forward, h to buy health potions per 10 GP, w to buy better weapon per 100 GP"
		elif self.type == 3:
			self.descr = "You see a blacksmith"
			self.hint = "Press a to go forward, w to upgrade weapon per 100 GP, r to buy better armor per 50 GP"
	def printDescr(self):
		print(self.descr)
	def printHint(self):
		print(self.hint)