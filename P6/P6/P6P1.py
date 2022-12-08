#CHAIN OF IF STATEMENTS?
with open('import.txt') as file:
    n=0
    line = file.readline()
    while n <= 4095:
        test = [line[n], line[n+1],line[n+2],line[n+3]]
        if test[0] != test[1] and test[0] != test[2] and test[0] != test[3]:
            if test[1] != test[2] and test[1] != test[3]:   
                if test[2] != test[3]:
                    print(n+4)
                    break
        n = n + 1            
   
