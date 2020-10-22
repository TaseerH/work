fname = input('Enter file: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1
#print(di)

tmp = list()
for k,v in di.items() :
    newt = (v,k)
    tmp.append(newt)
#print('flipped', tmp)
tmp = sorted(tmp, reverse=True)
#print('sorted', tmp[:5])
for v,k in tmp[:5] :
    print(k,v)
