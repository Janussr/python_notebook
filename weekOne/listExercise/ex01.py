x = range(1,21)

oddNumbers = [element for element in x if element % 2 != 0]

print(oddNumbers)

y = range(2,100001)

evenNumber = [element for element in y if element % 2 == 0]

print(min(evenNumber))
print(max(evenNumber))
print(sum(evenNumber))


n = range(3,301)

thirdNumber = [element for element in n if element % 3 == 0]

print(thirdNumber)


cubeRange = range(1,10)

cubeNumber = [element**3 for element in cubeRange ]

print(cubeNumber)