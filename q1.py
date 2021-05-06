def transpose(x,y):
    for i in range(len(x)):
        for j in range(len(x[0])):
            y[j][i]=x[i][j]
    for b in y:
        print(b)
def main():
    x=[[1,2],[3,4]]
    y=[[0,0],[0,0]]
    transpose(x,y)
if __name__=='__main__':
	main()
