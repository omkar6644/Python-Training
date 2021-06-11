#the below program adds 2 numbers represented as list.
a = [9,2,3,4]
s = [str(integer) for integer in a]
a_s = "".join(s)
n = int(a_s)
b = [9,5,4,3]
s1 = [str(integer) for integer in b]
a_s1 = "".join(s1)
m = int(a_s1)
sum = n+m
res = [int(x) for x in str(sum)]
print(res)

