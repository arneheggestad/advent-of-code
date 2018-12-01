inputFile = open('./data/input01.txt')

freq = 0

print('starting frequency: ', freq)

changes = inputFile.read()
changes = changes.splitlines()
for c in changes:
  freq = freq + int(c)

print('ending frequency: ', freq)
