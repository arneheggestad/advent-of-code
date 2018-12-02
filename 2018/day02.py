inputFile = open('./data/input02.txt')

testInput = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

exactlyTwo = 0
exactlyThree = 0

checksum = exactlyTwo * exactlyThree

inputs = inputFile.read()
inputs = inputs.splitlines()

# for i in testInput:
for i in inputs:
  isTwo = False
  isThree = False

  for l in i:
    c = i.count(l)
    if c is 2:
      isTwo = True
    if c is 3:
      isThree = True

  # print(i, isTwo, isThree)
  if isTwo is True:
    exactlyTwo = exactlyTwo + 1
  if isThree is True:
    exactlyThree = exactlyThree + 1

print('exactlyTwo: ', exactlyTwo)
print('exactlyThree: ', exactlyThree)
checksum = exactlyTwo * exactlyThree

print('checksum = ', checksum)


# part 2
testInput2 = ['acbde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

def compareBoxes(boxA, boxB):
  isDifferentByOneLetter = False
  commonLetters = 0
  tagLength = len(boxA)
  for i in range(tagLength):
    if boxA[i] is boxB[i]:
      commonLetters = commonLetters + 1
  # print('tag length: ', tagLength)
  # print('common letters: ', commonLetters)
  if commonLetters is tagLength - 1:
    # print(boxA, boxB)
    isDifferentByOneLetter = True
  return(isDifferentByOneLetter, boxA, boxB)

inputs = testInput2
for j in range(len(inputs)-1):
  for k in range(len(inputs)-j):
    (isDifferentByOneLetter, boxA, boxB) = compareBoxes(inputs[j], inputs[j+k])
    if isDifferentByOneLetter is True:
      print(boxA)
      print(boxB)
