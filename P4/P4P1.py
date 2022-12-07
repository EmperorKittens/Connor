

#use the range() function to get all the numbers in range.
#Compare both sides with set?
def makerange(split):
    #function that takes the split string and takes the numbers out and makes them two full ints
    #function needs to be able to makes sure that the array is a certain size so it does not error out.
    split2 = split.split('-')
    firstint = int(split2[0])
    secondint = int(split2[1]) + 1
    rng= list(range(firstint,secondint,1))
    return rng



with open('import.txt') as file:
    totalm = 0
    for lines in file.readlines():
        x = 0
        #Split the line in two.
        split = lines.split(',')
        #split them again into two numbers. Ex: 2-8 turns into 2,8
        n1 = split[0]
        n2 = split[1]
        r1= makerange(n1)
        r2 =makerange(n2)
        print(r1)
        if r1 in r2:
            x = x +1
        totalm =totalm + x 
print(totalm)


