import math

#A. Iterate a list of names to return a list of the names starting with H
names = ["Harald", "Ellen", "Herold", "Kurt", "Hans"]
newlist = []

for x in names:
  if "H" in x:
    newlist.append(x)

#print(newlist)




#B. in one line create a list of the numbers 1-100 to the power of 3

#powerOfThree = range(1,101)
#powerThree = [element**3 for element in powerOfThree ]
#print(powerThree)

#powerThreee = [element**3 for element in range(1,101)]
#print(powerThreee)

#print([element**3 for element in range(1,101)])



#C. Iterate a list of names to create a list of tuples where the tuples first value is the length of the name and the second is the name

names_with_tuples = ("Harald", "Ellen", "Herold", "Kurt", "Jan")

tuple_list = [(len(name), name) for name in names_with_tuples]
#print(tuple_list)




#D. Iterate over each character in a string and get only those that are nummeric

sentence = "5fladeflødebollerpå1fladtflødebollefad"
for element in sentence:
    if element in "0123456789":
       print(element)






#E.  Using only a list comprehension wrapped in set() get all possible combinations from throwing 2 dice (hint use 2 for loops in a single list comprehension). 
# Result should look like: [2,3,4,5,6,7,8,...] or a more complex/accurate solution: [(1,1),(1,2)...] in a way that (1,2) is equal to (2,1). 


dice1 = ['1','2','3','4','5','6']
dice2 = ['1','2','3','4','5','6']

dice_combinations = set([d1+' '+d2 for d2 in dice2 for d1 in dice1])
print(dice_combinations)





#A. Iterate a list of names and create a dictionary where key is the name and value is the length of the name

print({name: len(name) for name in names})


#B. Iterate a list of numbers and create a dictionary with {key:value} being {number:squareroot_of_number}

numbers = [5,10,50]
print({number: math.sqrt(number) for number in numbers})







#Extra assignment
dice_comb = [8, 6, 7, 8, 5, 10, 6, 8, 3, 7, 9, 4, 9, 11, 11, 6, 7, 9, 10, 4, 6, 10, 5, 8, 12, 4, 7, 7, 2, 5, 3, 7, 8, 6, 5, 9]

dice_dict = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

print({element: (dice_comb.count(element) / 36)*100 for element in dice_dict})
