a="khanh"
b="kqwrqeqweqwehqweqweqwaqweqweqwebqweqwenqweqweh"
dict={}
dict1={}
e=len(b)
s1=s2=0
check=True
for i in range(len(a)):
    if a[i]==" ":
        if i>=e:continue
        if b[i]==" ":continue
        c=b[i].lower()
        dict1[c]=1 if c not in dict1 else dict1[c]+1
        s2+=1
        continue
    else:
        c=a[i].lower()
        dict[c]=1 if c not in dict else dict[c]+1
        if i>=e:continue
        if b[i]==" ":continue
        c=b[i].lower()
        dict1[c]=1 if c not in dict1 else dict1[c]+1    
        s1+=1;s2+=1
for j in range(i+1,e):
    c=b[j].lower()
    dict1[c]=1 if c not in dict1 else dict1[c]+1
    s2+=1
if s2<s1:print(0)
else:
    for i in dict:
        if dict1[i]:
            if dict1[i]<dict[i]:print(0);check=False;break
        else:break
        if check==False:break
    else:print(1)