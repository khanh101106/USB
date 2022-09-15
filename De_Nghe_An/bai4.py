a=[int(input()) for _ in range(int(input()))]
res=1
for i in a:
    res*=i
cnt=0
for i in range(1,res+1):
    if res%i==0:cnt+=1
print(cnt)