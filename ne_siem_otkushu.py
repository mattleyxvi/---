def pathfinder(graph,start,end):
  startpath=[]
  endpath=[]
  path=0
  q=0
  if start==[0]:
      for j in range(len(end)-1,0,-1):
        endpath.append(end[j])
  for i in range(1,min(len(start),len(end))):
    if start[i]!=end[i] :
      for j in range(len(start)-1,i-1,-1):
        startpath.append(start[j])
      for j in range(len(end)-1,i-1,-1):
        endpath.append(end[j])
      break
    elif i==len(start)-1:
      for j in range(len(end)-1,i-1,-1):
        endpath.append(end[j])
      break
    elif i==len(end)-1:
      for j in range(len(start)-1,i-1,-1):
        startpath.append(start[j])
      break

  while(q<max(len(startpath),len(endpath))):
    if q<len(startpath):
      path+=graph[startpath[q]][0]
    if q<len(endpath):
      path+=graph[endpath[q]][0]
    q+=1
  
  return path
def chooseend(graph,start,apples):
  wae=pathfinder(graph,start,apples[0])
  ind=0
  c=0
  for i in apples:
    if wae<pathfinder(graph,start,i):
      wae=pathfinder(graph,start,i)
      ind=c
    c+=1
  return apples[ind]
def choosestart(graph,start,apples):
  wae=pathfinder(graph,start,apples[0])
  ind=0
  c=0
  for i in apples:
    if wae>pathfinder(graph,start,i):
      wae=pathfinder(graph,start,i)
      ind=c
    c+=1
  
  return apples[ind]

def chooseapple (start,apples,end):
  ind=0
  prior=0
  for j in range(len(apples)):
    if apples[j]!=end:
      for i in range(1,min(len(start),len(apples[j]))):
        if i==len(start)-1 and start[i]==apples[j][i]:
          if len(apples[j])>prior:
            prior=len(apples[j])
            ind=j
        elif start[i]!=apples[j][i]:
          if i>prior:
            prior=i
            ind=j
  #print(apples[ind])
  return apples[ind]



#asap glist make input
f = open('input_s1_23.txt','r')
vetki=[[0]]
path=0
apples=[]
apples_sort=[]
a= f.readline().split(' ')
for i in range(int(a[0])):
  q=f.readline().split(' ')
  vetki.append([int(q[1])])
  for k in range(1,len(vetki[int(q[0])])):
    vetki[-1].append(vetki[int(q[0])][k])
  vetki[-1].append(len(vetki)-1)
  
for i in range(int(a[1])):
  q=f.readline().split(' ')
  apples.append(vetki[int(q[0])])
  apples_sort.append(int(q[1]))
  
q=f.readline().split(' ')
start=vetki[int(q[0])]
for i in range(len(apples_sort)):
  if apples_sort[i]<int(q[1]):
    apples[i]=[]
while([] in apples):
  apples.remove([])
#print(apples)
end=chooseend(vetki,start,apples)   
while len(apples)!=0:
  path+=pathfinder(vetki,start,chooseapple(start,apples,end))
  au=chooseapple(start,apples,end)
  start=au
  apples.remove(au)
path+=pathfinder(vetki,start,end)
print(path)




