with open('import.txt') as file:
    n=0
    for line in file.readlines():
            while n < 4096:
                test = set(line[n: n+14])
                if len(test) == 14:
                    print(n + 14)
                    break
                n= n + 1
# i hate everything