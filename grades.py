no= input('enter a number between 0.0 and 1.0')
try:
    fvalue = float(no)
except:
    print('Invalid Input')
    exit()
if fvalue >=0.9:
    print('A')
elif fvalue >=0.8:
    print('B')
elif fvalue >= 0.7:
    print('C')
elif fvalue >=0.6:
    print('D')
else:
    print('F')
