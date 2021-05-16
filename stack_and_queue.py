print("STACK OPERATION")
s=[0,0,0,0,0]
for i in range(len(s)):
    n=int(input("enter elements :"))
    s[i]=n
print()
print("Stack after inserting the elements :")
print(s)
print()
print("stack after popping")
for i in range(len(s)-1,-1,-1):
    print(s[:i])
print()
print()
print("QUEUE OPERATION")
s=[0,0,0,0,0]
for i in range(len(s)):
    n=int(input("enter elements :"))
    s[i]=n
print()
print("Queue after inserting the elements")
print(s)
print()
print("Queue after popping :")
for i in range(1,len(s)+1):
    print(s[i:])





