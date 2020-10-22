#with loop
#total = 0
#count = 0
#while True :
#    inp = input('Enter a number: ')
#    if inp == 'done' : break
#    value = float(inp)
#    total = total + value
#    count = count + 1

#average = total / count
#print('Average1 : ', average)
#with lists
numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average2 :', average)
