def reroll(val,unl,order):
    for i in range(len(val)):
        for j in range(len(unl)):
            if val[i]>=unl[j]:
                val[i]-=order
    return val
def swap(val,exc,order):
    newval=[]
    out=[]
    if order==1:
        for i in range(len(val)):
            for j in range(i+1,len(exc)):
                val[i]*=exc[j]
        return sum(val)
    elif order==-1:
        for i in range(len(exc)-1,0,-1):
            newval.append(val%exc[i])
            val=val//exc[i]
            if i==1:
                newval.append(val)
        for i in reversed(newval):
            out.append(i)
        return out

f=open("input13.txt")
a=[]
order=1
val=0
for i in range(5):
    a.append(f.readline().split(' '))
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j]=int(a[i][j])
a[1].pop(0)
a[3].pop(0)
a[1].sort(reverse=True)
a[3].sort()
a[4]=reroll(a[4],a[1],order)
val=swap(a[4],a[0],order)
order=-1

a[4]=swap(val,a[2],order)
a[4]=reroll(a[4],a[3],order)

        
print(a[4])
