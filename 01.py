import math
rawPuzzleInput = open('puzzle_input.txt')
puzzleInput = rawPuzzleInput.read()

moduleMasses = puzzleInput.split('\n')

def calculateFuelFromMass(mass):
  fuel_required = math.floor(mass/3) - 2
  return fuel_required

totalFuelAmount = 0

# Part 2
for massString in moduleMasses:
  current = int(massString)
  while current > 0:
    newAmount = calculateFuelFromMass(current)
    if newAmount > 0:
      totalFuelAmount += newAmount
    
    current = newAmount

print(totalFuelAmount)
# 3226488
# 4836845