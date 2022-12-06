#make functions to win against each variable
def win(opp, x, totalm):
    if opp == 'A':
        x = x + 8
    elif opp == 'B':
        x = x + 9
    elif opp == 'C':
        x = x + 7
    totalm = totalm + x
    return totalm
#make functions to draw against each variable
def draw(opp, x,totalm):
    if opp == 'A':
        x = x + 4
    elif opp =='B':
        x = x + 5
    elif opp == 'C':
        x = x + 6
    totalm = totalm + x
    return totalm 
#make functions to lose against each variable
def loss(opp, x,totalm):
    if opp == 'A':
        x = x + 3
    elif opp == 'B':
        x = x + 1
    elif opp == 'C':
        x = x +2
    totalm = totalm + x
    return totalm
with open('import.txt') as file:
    totalm = 0
    x = 0
    for line in file.readlines():
        #reset x
        x = 0
        #make functions to get strings out of arrays
        sline = line.strip()
        me = str(sline[2])
        opp = str(sline[0])
        #call funtions based on what the value of me is. x is lose, y is draw, and z is win
        if me == 'X':
            totalm = loss(opp,x,totalm)
        elif me == 'Y':
            totalm = draw(opp,x, totalm)
        elif me == 'Z':
            totalm = win(opp,x, totalm)
        
        #print(x)
       
        
        #logic for rock, paper, scissors

print(totalm)
