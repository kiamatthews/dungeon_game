### LIBARIES ###
import random
import os
import sys

### VARIABLES/COLLECTIONS ###
#5x5 grid made up of x and y coordinates
CELLS = [(0,0),(1,0),(2,0),(3,0),(4,0),
         (0,1),(1,1),(2,1),(3,1),(4,1),
         (0,2),(1,2),(2,2),(3,2),(4,2),
         (0,3),(1,3),(2,3),(3,3),(4,3),
         (0,4),(1,4),(2,4),(3,4),(4,4)]

### FUNCTIONS ###

def clear_screen():
  os.system ('cls' if os.name == 'nt' else 'clear')

def get_locations():
  return random.sample(CELLS, k=3)

def get_moves(player):
  moves = ["LEFT", "RIGHT", "UP", "DOWN"]
  x, y = player
  if x == 0:
    moves.remove("LEFT")
  if x == 4:
    moves.remove("RIGHT")
  if y == 0:
    moves.remove("UP")
  if y == 4:
    moves.remove("DOWN")
  return moves

def move_player(player, move):
  #get the players location
  x, y = player
  #Good move? Move player position
  #Bad move (i.e. out of bounds)? Dont move player and warn about boundaries
  if move == "LEFT" and x == 0:
    print("You can't move left.")
  elif move == "LEFT":
    x -= 1
  elif move == "RIGHT" and x == 4:
    print("You can't move right.")
  elif move == "RIGHT":
    x += 1
  elif move == "UP" and y == 0:
    print("You can't move up.")
  elif move == "UP":
    y -= 1
  elif move == "DOWN" and y == 4:
    print("You can't move down.")
  elif move == "DOWN":
    y += 1
  return x, y

def draw_map(player):
  print(" _"*5)
  tile = "|{}"

  for cell in CELLS:
    x, y = cell
    if x < 4:
      line_end = ""
      if cell == player:
        output = tile.format("X")
      else:
        output = tile.format("_")
    else:
      line_end = "\n"
      if cell == player:
        output = tile.format("X|")
      else:
        output = tile.format("_|")
    print(output, end=line_end)


def game_loop():
  player, door, monster = get_locations() #pick random location for player, door and monster
  while True:
    draw_map(player)
    print("You are currently in room {}".format(CELLS.index(player) + 1)) # fill with player position
    print("You can move {}".format(", ".join(get_moves(player)))) #fill with available moves
    print("Enter QUIT to quit."),

    move = input("> ").upper()#take input from player for movement

    if move == "QUIT":
      sys.exit()
    else:
      clear_screen()
      player = move_player(player, move)#move player, unless past edges of grid
      #check for win/loss
      if player == door: #On the door? YOU WIN
        print("\n *** You've escaped the dungeon! *** \n")
        again = input("Play again? [Y/n]: ")
        if again.lower() == "n":
          print("\n *** Good bye intrepid explorer! *** \n")
          sys.exit()
        else:
          continue
      elif player == monster: #On the monster? YOU LOSE
        print("\n *** Oh, no. You have just been disembowled by a gruesome monster. Sorry dude. *** \n")
        sys.exit()
      else:
        continue

      #clear screen and redraw grid

#game loop
while True:
  print("Welcome to the dungeon!")
  input("Press enter to begin")
  clear_screen()
  game_loop()
