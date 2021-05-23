class Sort:
    #function to perform bubble sort
    def bubble(self):
        a = [5, 3 , 2 , 4 , 0 , 1]
        n = len(a)
        for i in range(0, n-1):
            for j in range(0 , n-i-1):
                if( a[j] > a[j+1] ):
                    temp = a[j]
                    a[j] = a[j+1]
                    a[j+1] = temp
        for i in range(0,n):
            print(a[i])
    
S = Sort()
print("sorted array is :")
S.bubble()



