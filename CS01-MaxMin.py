loop = int(input('Enter loop : '))
Total = []

for i in range(loop):
    num = int(input('Enter your number: '))
    Total += [num]
Total.sort()
print(Total[0])
print(Total[-1])



