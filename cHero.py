import random
import cWorld

c_restCost = 5
c_HPCost = 10
c_weaponCost = 100
c_armorCost = 50
c_weaponUpgradeCost = 50
c_potionHeal = 20
c_potionHeal = 20
c_armorPerLevel = 5
c_dmgPerLevel = 15
c_maxArmorLevel = 3
c_maxWeaponLevel = 3
c_maxWeaponUpgrade = 3

class Hero:
	def __init__(self):
		self.health = 100
		self.mana = 100
		self.exp = 0
		self.level = 1
		self.armor_level = 1
		self.armor_upgrade = 0
		self.weapon_level= 1
		self.weapon_upgrade = 0
		self.world = 1
		self.zone = 1
		self.potions  = 3
		self.gold  = 10
		self.lastMsg = ""
		
	def showStats(self):
		print("HP:" + str(self.health) + " MP:" + str(self.mana) + " level:" + str(self.level) + " EXP:" + str(self.exp) + " GP " + str(self.gold) +  "\nArmor: " + self.getArmorVal() + "\nWeapon: " + self.getWeaponVal() + "\nWorld: " + str(self.world) + "-" + str(self.zone) + "\n" + "You have " + str(self.potions) + " healing potions")
	
	def printLastMsg(self):
		print(self.lastMsg)
		
	def getMaxHealth(self):
		return (self.level - 1) * 10 + 100
		
	def rest(self):
		if self.gold >= c_restCost:
			self.health = self.getMaxHealth()
		else:
			self.lastMsg = "Not enough money"
			
	def buyHealthPotion(self):
		if self.gold >= c_HPCost:
			self.potions += 1
			self.gold -= c_HPCost
		else:
			self.lastMsg = "Not enough money"
			
	def buyWeapon(self):
		if self.gold >= c_weaponCost:
			if self.weapon_level <= c_maxWeaponLevel:
				self.weapon_level += 1
				self.weapon_upgrade = 0
				self.gold -= c_weaponCost
			else:
				self.lastMsg = "You already have best weapon"
		else:
			self.lastMsg = "Not enough money"
			
	def buyWeaponUpgrade(self):
		if self.gold >= c_weaponUpgradeCost:
			if self.weapon_upgrade <= c_maxWeaponUpgrade:
				self.weapon_upgrade += 1
				self.gold -= c_weaponUpgradeCost
			else:
				self.lastMsg = "You already have maximum upgrade level"
		else:
			self.lastMsg = "Not enough money"
			
	def buyArmor(self):
		if self.gold >= c_armorCost:
			if self.armor_level <= c_maxArmorLevel:
				self.armor_level += 1
				self.armor_upgrade = 0
				self.gold -= c_armorCost
			else:
				self.lastMsg = "You already have best armor"
		else:
			self.lastMsg = "Not enough money"
			
	def drinkHP(self):
		if self.potions > 0:
			self.health = min(self.getMaxHealth(), self.health + c_potionHeal)
			self.potions -= 1
		else:
			self.lastMsg = "Not enough potions"
		
	def attack(self, world):
		self.health = self.health - max(world.zones[self.zone].attack - self.armor_level * c_armorPerLevel + self.armor_upgrade, 0)
		world.zones[self.zone].health = world.zones[self.zone].health - max(c_dmgPerLevel * self.weapon_level + self.weapon_upgrade - world.zones[self.zone].defence, 0)
		self.lastMsg = "You attack the monster"
		return world
		
	def flee(self, world):
		if len(world.zones) == self.zone:
			self.lastMsg = "You can't flee from the world Boss"
			return world
		self.health = self.health - max(world.zones[self.zone].attack - self.armor_level * c_armorPerLevel + self.armor_upgrade, 0)
		rnd = int(random.random() * 1)
		if rnd == 0:
			world = self.move(world)
		return world
		
	def move(self, world):
		if self.zone ==  len(world.zones) - 1:
			self.world += 1
			self.zone = 1
			self.lastMsg = "You entered into new world"
			return cWorld.World(self.world)
		else:
			self.zone += 1
			self.lastMsg = "You entered into new area"
			return world
			
	def getArmorVal(Hero):
		buf = "11"
		if Hero.armor_level == 1:
			buf = "leather jacket" 
		elif Hero.armor_level == 2:
			buf = "iron mail" 
		elif Hero.armor_level == 3:
			buf = "steel plate"
		elif Hero.armor_level == 4:
			buf = "magic plate"
		if Hero.armor_upgrade != 0:
			buf += " + " + str(Hero.armor_upgrade)
		return buf
	
	def getWeaponVal(Hero):
		buf = "11"
		if Hero.weapon_level == 1:
			buf = "iron sword" 
		elif Hero.weapon_level == 2:
			buf = "steel sword" 
		elif Hero.weapon_level == 3:
			buf = "flame sword"
		elif Hero.weapon_level == 4:
			buf = "holy sword"
		if Hero.weapon_upgrade != 0:
			buf += " + " + str(Hero.weapon_upgrade)
		return buf	