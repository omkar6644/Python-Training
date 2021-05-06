a=[1,3,6,9,10]
n=len(a)
sum=12
for i in range(0, n):
    for j in range(i+1,n):
        if(a[i]+a[j] == sum):
            print("position of {} and {} are".format(a[i],a[j]),a.index(a[i]),a.index(a[j]))

