inputFile = open('./data/input02.txt')

testInput = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

exactlyTwo = 0
exactlyThree = 0

checksum = exactlyTwo * exactlyThree

for i in testInput:
  isTwo = False
  isThree = False

  for l in i:
    c = i.count(l)
    if c is 2:
      isTwo = True
    if c is 3:
      isThree = True

  print(i, isTwo, isThree)
  if isTwo is True:
    exactlyTwo = exactlyTwo + 1
  if isThree is True:
    exactlyThree = exactlyThree + 1

print('exactlyTwo: ', exactlyTwo)
print('exactlyThree: ', exactlyThree)
checksum = exactlyTwo * exactlyThree

print('checksum = ', checksum)


