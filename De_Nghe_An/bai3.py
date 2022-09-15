from  collections import defaultdict
a=int(input())
b=[int(input()) for _ in range(a)]
dict=defaultdict(list)
for i in b:
    dict[i]=1 if i not in dict else dict[i]+1
m=1000000000
for i in dict:
    if dict[i]==1:m=min(m,i)
print(m)