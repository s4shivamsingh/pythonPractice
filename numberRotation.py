arr=list(input().split())
n=len(arr)-2
k=int(arr[-1])
var=[]
l1=[]
l2=[]

for i in range(1,len(arr)-1):
    var.append(arr[i])
t=len(var)-k
l2.append(var[0])
for i in range(len(var)):
    if i<t:
        l1.append(var[i])
    else:
        l2.append(var[i])

l1.pop(0)
total=l2+l1
print(total)
