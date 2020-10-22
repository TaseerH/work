num = -1
print ('At Start', num)
while True :
    sval = input('Enter a number: ')
    if sval == 'Done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
for Num in [2, 4, 7, 10] :
    if Num > num :
        num = Num
smallest = None
for value in [2, 4, 7, 10] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
print('After', 'Largest' , num, 'Smallest', smallest)
