#make an array of arrays
#move objects from arrays into other arrays
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []
a7 = []
a8 = []
a9 = []
#make function that takes in the amount needed to move and them act on specific parts of the dictionary
def move(moveint,onint,toint):
    #first things first sub 1 off onint and toint because of array indexing
    onint = int(onint -1)
    toint = int (toint -1)
    temp = main[onint][0:moveint]
    main[toint] = temp + main[toint]
    del main[onint][0:moveint]
    


 
    return 
def clearspace(array):
    #make a function to clear the blank spot out of the array
    n = 0
    for i in array:
        if '   ' in array[n]:
            del array[n]     
    return array

with open('import.txt') as file:
    for lines in file.readlines():
        if lines[0] == ' ':
            break
        a1.append(lines[0:3])
        a2.append(lines[4:7])
        a3.append(lines[8:11])
        a4.append(lines[12:15])
        a5.append(lines[16:19])
        a6.append(lines[20:23])
        a7.append(lines[24:27])
        a8.append(lines[28:31])
        a9.append(lines[32:35])
#have to call this function one at a time or it returns after the first loop....
clearspace(a1)
clearspace(a2)
clearspace(a3)
clearspace(a4)
clearspace(a5)
clearspace(a6)
clearspace(a7)
clearspace(a8)
clearspace(a9)
#dont know why but the script to clear didnt get this one....
del a2[0]
#turn all arrays into a dictionary
main = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
#practice moving arrays in dictionaries
import re
with open('import.txt') as file:
    for lines in file:
        if lines[0] == 'm':
            #split lines in half 
            firsth = lines[:len(lines)//2]
            secondh = lines[len(lines)//2:]
            # split again for the second half to get 2 numbers
            onsplit = secondh[:len(secondh)//2]
            tosplit = secondh [len(secondh)//2:]
            #search for numbers and group them.
            onint = int(re.search(r'\d+',onsplit).group())
            toint = int(re.search(r'\d+',tosplit).group())
            moveint = int(re.search(r'\d+', firsth).group())
            move(moveint, onint,toint)




print(main)

        


