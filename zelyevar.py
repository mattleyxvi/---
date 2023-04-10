def convert_spell(spell,prev):
    auba=spell.split(' ')
    spname=''
    spinit=''
    if auba[0]=='DUST':
        spname='DT'
    elif auba[0]=='WATER':
        spname='WT'
    elif auba[0]=='MIX':
        spname='MX'
    elif auba[0]=='FIRE':
        spname='FR'
    for i in range(1,len(auba)):
        if auba[i].isalpha():
            spinit+=auba[i]
        else:
            spinit+=prev[int(auba[i])-1]
    return spname+spinit+spname[1]+spname[0]
f = open('input10.txt','r')
file=f.read().split('\n')
prev=[]
for i in file:
    prev.append(convert_spell(i,prev))

f2=open('output10.txt','r')
if f2.read()==prev[-1]:
    print('boba')

