import sys
import os
import random
import cHero
import cWorld




	
def die():
	print("You die")
	print("Game over")
	buf = input("Press a key to leave: ")
	sys.exit(0)
		
def win():
	print("You won\n")
	print("Game over\n")
	buf = input("Press a key to leave: ")
	sys.exit(0)


player = cHero.Hero()
world = cWorld.World(1)
world.printDescr(8)
lastMsg = ""
while 1 == 1:
	#clear screen
	os.system('cls' if os.name == 'nt' else 'clear')
	player.showStats()
	player.printLastMsg()
	world.printDescr(player.zone)
	world.printHint(player.zone)
	if world.zones[player.zone].type == 0:
		world.printEnemyStats(player.zone)
	buf = input("Press a key: ")
	if world.zones[player.zone].type == 0:
		if buf == 'a':
			world = player.attack(world)
			print(player.health)
			if player.health <= 0:
				die()
			elif world.zones[player.zone].health <=0:
				player.exp += world.zones[player.zone].exp
				player.gold += world.zones[player.zone].gold
				if player.exp >= player.level * 10 + 100:
					player.level += 1
					player.health = player.getMaxHealth()
					player.exp = 0
				world = player.move(world)
		elif buf == 'f':
			world = player.flee(world)
			if player.health <= 0:
				die()
		elif  buf == 'h':
			player.drinkHP()
		else:
			player.lastMsg = "Unknown command"
	elif world.zones[player.zone].type == 1:
		if buf == 'r':
			player.rest()
			world = player.move(world)
		elif buf == 'a':
			world = player.move(world)
		else:
			player.lastMsg = "Unknown command"
	elif world.zones[player.zone].type == 2:
		if buf == 'h':
			player.buyHealthPotion()
		elif buf == 'w':
			player.buyWeapon()
		elif buf == 'a':
			world = player.move(world)
		else:
			player.lastMsg = "Unknown command"
	elif world.zones[player.zone].type == 3:
		if buf == 'r':
			player.buyArmor()
		elif buf == 'w':
			player.buyWeaponUpgrade()
		elif buf == 'a':
			world = player.move(world)
		else:
			player.lastMsg = "Unknown command"
	if player.world == 9:
		win()
