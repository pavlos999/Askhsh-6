import random
from pprint import pprint
import sys

def num_change(x, y, minesweeperArray):
  for i in range(x - 1, x + 2):
    for n in range(y - 1, y + 2):
      try:
        if(minesweeperArray[i][n] != -1):
          minesweeperArray[i][n] += 1
      except:
        pass


try:
  dimensionX = input("Give me x size: ")
  dimensionY = input("give me y size: ")
  mines = input("Give me number of mines(0 < number < x*y): ")
  if(mines < 0 or (mines > dimensionX*dimensionY)):
    raise Exception()
except:
  print("Input was not valid")
  sys.exit()
minesweeperArray = [[0 for y in range(dimensionY)] for x in range(dimensionX)]
while(mines>0):
  r1 = random.randint(0, dimensionX - 1)
  r2 = random.randint(0, dimensionY - 1)
  if(minesweeperArray[r1][r2] == 0):
    minesweeperArray[r1][r2] = -1
    mines -= 1
pprint(minesweeperArray)
for x in range(dimensionX - 1):
  for y in range(dimensionY - 1):
    if(minesweeperArray[x][y] == -1):
      num_change(x, y, minesweeperArray)
pprint(minesweeperArray)
