print('Hello World')
n=input('who r u?')
print('wellcome' , n )
x= int(input('your number?'))
if x== 5 :
    print('equals 5')
if x>4 :
    print('Greater than 4')
if x>= 5 :
    print('Greater than or equal to 5')
if x<6 : print ('less than 6')
if x<=5 :
    print('Less than or equal to 5')
if x!= 6 :
    print('not equal to 6')
if x>3 :
    print ('Bigger')
else :
    print ('smaller')
try:
    m = int(n)
except:
    m = 1
print('First', m)

try:
    m= int(x)
except:
    m = 1
print ('Second', m)
