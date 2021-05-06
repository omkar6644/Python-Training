def clockwise(a):
    for j in range(2) :
        for i in range(2-1,-1,-1):
            print(a[i][j], end = " ")
        print()
def main():    
    a=[[ 1, 2, 3],[ 4,5,6]]
    n=input("enter the direction:   ")
    if n=="clockwise":    
        clockwise(a);
    else:
        print("enter a valid direction")

if __name__=='__main__':
    main()
