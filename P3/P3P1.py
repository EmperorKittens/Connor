
#give letters numerical value.
def conversionl(output):
    number = ord(output) - 96
    return number
def conversionu(output):
    number = ord(output) - 65 + 27
    return number
    



#import text
#divide text in half    
with open('Import.txt') as file:
    total = 0
    for line in file.readlines():
        firsth = line[:len(line)//2]
        secondh = line[len(line)//2:]
        x = 0
        #compare for like letters (case sensitive)
        compare = str(set(firsth) & set(secondh))
        output = compare.strip()
        print(output)
        if output.islower():
            x = conversionl(output[2])
        else:
            x = conversionu(output[2])
        total = total + x    
print(total)
    
