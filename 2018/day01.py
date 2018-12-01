inputFile = open('./data/input01.txt')

startingFreq = 0
startingFreqs = []

print('starting frequency: ', startingFreq)

# changes = inputFile.read()
# changes = changes.splitlines()
# changes = [3, 3, 4, -2, -4]
changes = [7, 7, -2, -7, -4]

def doChanges(freq, freqs, dupe):
  for c in changes:
    if freq in freqs:
      print('duplicate frequency: ', freq)
      freqs.append(freq)
      dupe = True
    else:
      freqs.append(freq)
    freq = freq + int(c)

  return(freq, freqs, dupe)

(endingFreq, existingFreqs, duplicateFound) = doChanges(startingFreq, startingFreqs, False)
print('ending frequency from fx: ', endingFreq)
while duplicateFound is False:
  (endingFreq, existingFreqs, duplicateFound) = doChanges(endingFreq, existingFreqs, duplicateFound)
  print('ending frequency from fx: ', endingFreq)
