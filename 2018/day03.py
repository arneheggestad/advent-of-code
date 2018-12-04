inputFile = open('./data/input03.txt')
import re

testClaims = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']

# claims = testClaims

claims = inputFile.read()
claims = claims.splitlines()

def parseClaim(claim):
  regex = r"#(\d*) @ (\d*),(\d*): (\d*)x(\d*)"
  match = re.search(regex, claim)
  (claimNumber, xStart, yStart, width, height) = match.groups()
  claimNumber = int(claimNumber)
  xStart = int(xStart)
  yStart = int(yStart)
  width = int(width)
  height = int(height)
  return (claimNumber, xStart, yStart, width, height)

claimedArea = []
conflicts = []
duplicatedArea = []

for claim in claims:
  parsedClaim = (parseClaim(claim))
  # print(parsedClaim)
  (claimNumber, xStart, yStart, width, height) = parsedClaim

  claimConflicts = False

  for i in range(0, width):
    for j in range(0, height):
      newClaim = (xStart + i, yStart + j)
      if newClaim in claimedArea:
        conflicts.append({'claim': claimNumber, 'coords': newClaim})
        claimConflicts = True
        if newClaim not in duplicatedArea:
          duplicatedArea.append(newClaim)
      else:
        claimedArea.append(newClaim)

  if claimConflicts is True:
    print(claimNumber, ' conflicts with previous claims')

# print(claimedArea)
# print(conflicts)
print('duplicate area: ', len(duplicatedArea))
