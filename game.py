print("RollPy")
print("Installing Addons...")
import time
import random as rand
import math
print("Preparing game for launch...")
time.sleep(3)
hp = 100
print("WELCOME TO ROLLPY, A TEXT BASED RPG BUILT IN PYTHON.")
time.sleep(1)
uname = input("WHAT IS YOUR NAME, ADVENTURER?")
questSelection = int(input("WHAT IS YOUR QUEST? (1 - TO FIND THE SECRETS, 2 - TO GET AS MUCH GOLD AS POSSIBLE, 3 - TO GET TROLLED MASSIVELY)"))
irrelevantinbox9268726381622921 = print("WHAT IS... wait i forgot")
time.sleep(0.5)
print("Anyways, move along now, " + uname +". Dangers lead up ahead.")
time.sleep(5)
if questSelection == 1:
  print('You find a hidden walkway with a sign that says "BEWARE ' + uname + ', THE SECRETS ARE TOO SCARY"')
  wordWritten = input("What will you respond with on the sign? (this cannot be skipped its important to the LORE ¯\_(ツ)_/¯ )")
  print('You wrote "' + wordWritten + '" on the sign.')
  whatdoyoudo = input("What will you do now? (1 - Go down the hallway, 2 - Wait by the sign)")
  if whatdoyoudo == 1:
    print("You travel down the hallway and come across two branches. One is further away from the other. You cannot see what's inside. The other is boarded up, but you hear the sound of wood being punched, and lasers.")
    time.sleep(0.25)
    whatdoyoudo = input("Where will you go? (1 - Investigate the boarded up room, 2 - Go down the hallway")
    if whatdoyoudo == 1:
      print("You attempt to break open the boarded room.")
      print("Rolling for strength...")
      time.sleep(3)
      roll = rand.randint(1, 20)
      opposingroll = rand.randint(1, 20)
      print(roll + ".")
      if roll > opposingroll:
        print("You succesfully broke the wooden barrier and ran into the room.")
        roll = rand.randint(1, 20)
      if roll < 10:
        print("The robots prepared for attack.")
        losthp = rand.randint(1, 20)
        hp = hp - (losthp * 2.5)
        print("You lost " + losthp + ", which means you now have only " + hp + " left.")
    elif roll <= opposingroll:
      print("You failed at breaking the wooden barrier. (It's probably for the best.)")
      time.sleep(1)
elif questSelection == 2:
  print("You find piles of gold. Mountains of gold. But you can only carry 10 tons of gold at a time with the help of some friends. At the moment, you have no friends, so you can only carry 1/3 of that gold.")
  whatdoyoudo = input("What will you do? (1 - Wait in the gold room, 2 - Begin to steal gold, 3 - Follow the strange hallway leading to the room.)")
  if whatdoyoudo == 1:
    print("You wait...")
    time.sleep(5)
    print("...and wait...")
    time.sleep(10)
    print("...and wait some more...")
    time.sleep(15)
    print("You feel like there isn't a point in waiting anymore.")
    roll = rand.randint(1, 20)
    if roll => 7:
      print("Suddenly, a clone of you ran in from the mysterious hallway.")
      if roll => 14:
        print("They are followed up by another person who looks identical to you.")
    else:
      print("You are all alone.")
      print("Congrats, you played yourself.")
elif questSelection == 3:
  print("You find yourself in a dark room with a small hallway boarded up. You feel a sense of impending doom. Suddenly, 3 AI robots, with pictures of a rickroll, a troll face, and a cat, fall from the ceiling chasing after you with deadly lasers.")
  whatdoyoudo = ("What will you do? (1 - Break the hallway barrier, 2 - Grab a mace from the corner (where did that come from?) and destroy the robots, 3 - Throw the robots against the wall and pin them down.)")
  if whatdoyoudo == 1:
    print("Rolling for strength...")
    time.sleep(3)
    roll = rand.randint(1, 20)
    opposingroll = rand.randint(1, 20)
    print(roll + ".")
    time.sleep(1)
    if roll > opposingroll:
      print("You succesfully broke the wooden barrier and ran into the hallway.")
    elif roll <= opposingroll:
      print("You failed at breaking the wooden barrier. That gave the robots a free chance to attack.")
      time.sleep(1)
      losthp = rand.randint(1, 20)
      hp = hp - (losthp * 2.5)
      print("You lost " + losthp + ", which means you now have only " + hp + " left.")
else:
  print("That is not an option, " + uname + ", you have to pick options 1-3.")
