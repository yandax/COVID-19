print("Hello, World!")

# name = input("best country in the world: ")
# print(name)

'''
lowername = name.lower()
if (lowername == "canada"):
    print(name + " is the best")
elif (lowername == "norway"):
    print(name + " is the 2nd best")
else:
    print("booo wrong answer")
'''

fruits = ['apple,grannysmith,gala', 'orange,mandarin,bloodorange', 'banana,big,small', 'peach,sweet,not sweet']

for fruit in fruits:
    templist = fruit.split(",")
    print(fruit)
    print(templist)
    for i in templist:
        print(i)
