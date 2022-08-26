a="hi am fabev!34y"
b=""
d=''
c=[]
list1=["a","e"," ","i","o","u" ]
for x in range(len(a)):
    y = a[x].isalpha()

    if(y):
      if a[x] not in list1:
            
       c.append(a[x])
       b+=a[x]
      else:
        d+=a[x]
print(c)
print(b)
print(d)
print(len(c))

    
