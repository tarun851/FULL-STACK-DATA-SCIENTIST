str=input("enter space seperated values:")
a=[int(x) for x in str.split(" ")]
a=set(a)
a=list(a)
a.sort(reverse=True)
print(a[1])
