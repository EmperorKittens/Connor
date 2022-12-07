

#use the range() function to get all the numbers in range.
#Compare both sides with set?
def makerange(split):
    #function that takes the split string and takes the numbers out and makes them two full ints
    split2 = split.split('-')
    firstint = int(split2[0])
    secondint = int(split2[1]) + 1
    #gets a range of numbers based on the first number second number. ex: 50-60 turns into a range of 50 to 60. output is 50, 51, 52, 53, 54,55,56,57,58,59,60
    rng= list(range(firstint,secondint,1))
    return rng
def fullycontains(range1, range2):
    if set(range1).intersection(range2):
        return 1
    return 0

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
        #print(r1)
        x= fullycontains(r1, r2)
        totalm =totalm + x
print(totalm)


