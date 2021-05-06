a=[1, 2, 3,4]
s=[str(integer) for integer in a]
a_s="".join(s)
n=int(a_s)
b=[8,6]
s1=[str(integer) for integer in b]
a_s1="".join(s1)
m=int(a_s1)
sum=n+m
res=[int(x) for x in str(sum)]
print(res)

