import cZone

class World:
	def __init__(self, world):
		while 1 == 1:
			self.zones = []
			for i in range(0,9):
				self.zones.append(cZone.Zone(world))
			if self.zones[len(self.zones) - 1].type != 0:
				continue
			cntMonster = 0
			for i in self.zones:
				if i.type == 0:
					cntMonster += 1
			if cntMonster == len(self.zones) or cntMonster < len(self.zones) / 2:
				continue
			if self.zones[1].type != 0 or self.zones[0].type != 0:
				continue
			break
		self.zones[len(self.zones) - 1].health = self.zones[len(self.zones) - 1].health * 2
		if world == 8 :
			self.zones[len(self.zones) - 1].health = self.zones[len(self.zones) - 1].health * 2
			self.zones[len(self.zones) - 1].attack = self.zones[len(self.zones) - 1].attack * 2
			self.zones[len(self.zones) - 1].defence = self.zones[len(self.zones) - 1].defence * 2
			self.zones[len(self.zones) - 1].descr = "You see a great Dragon. It's your last enemy"
	def printDescr(self, index):
		print(self.zones[index].descr)
	def printHint(self, index):
		print(self.zones[index].hint)
	def printEnemyStats(self, index):
		print("Enemy HP: " + str(self.zones[index].health) + " enemy defence: " + str(self.zones[index].defence) + " enemy attack: " + str(self.zones[index].attack))