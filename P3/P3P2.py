


def conversionl(output):
    number = ord(output) - 96
    return number
def conversionu(output):
    number = ord(output) - 65 + 27
    return number
def snip(segment):
    output = segment.strip()
    return output

#split incoming data
#segment = content[2]
#snip = segment.strip()

#for loop with iterating segmants of the file (by 3)
#stop when n0 = n1
n0 = 0
n1 = 0
n2 = 0 
file = open('Import.txt') 
content = file.readlines()
total = 0
while n2 != 300:
    segment0 = content[0 + n0]
    n0 = n0 + 3
    segment1 = content[1 + n1]
    n1 =n1 + 3
    segment2 = content[2 + n2]
    n2 =n2 +3
    segment0 = snip(segment0)
    segment1 = snip(segment1)
    segment2 =snip(segment2)
    compare = str(set(segment0) & set(segment1) & set(segment2))
    #print (compare)
    x = 0
        #compare for like letters (case sensitive)
    if compare.islower():
        x = conversionl(compare[2])
    else:
        x = conversionu(compare[2])
    total = total + x    
print(total)