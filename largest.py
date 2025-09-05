a=[]
max=0
for i in range(5):
    v=int(input())
    a.append(v)
for j in a:
    if j>max:
        max=j
print("max :",max)