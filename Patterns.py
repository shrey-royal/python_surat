'''
1 2 3 4 
1 2 3 
1 2 
1 


n = int(input("Enter the number of rows: "))
i = n
while(i >= 1):
    j=1
    while(j<=i):
        print(j,end=" ")
        j+=1
    print()
    i-=1
'''

'''
1 2 3 4 
2 3 4 
3 4 
4 

n = int(input("Enter the number of rows: "))
i = 1
while(i <= n):
    j = i
    while(j <= n):
        print(j,end=" ")
        j+=1
    print()
    i+=1
'''
'''
4 3 2 1 
3 2 1 
2 1 
1 

n = int(input("Enter the number of rows: "))
i = n
while(i >= 1):  # this loop is responsible for printing the rows
    j = i
    while(j >= 1):  # this loop is responsible for printing the columns
        print(j,end=" ")
        j-=1
    print()
    i-=1
'''

'''
4 3 2 1 
4 3 2 
4 3 
4 

n = int(input("Enter the number of rows: "))
i = 1
while(i <= n):
    j = n
    while(j >= i):
        print(j,end=" ")
        j-=1
    print()
    i+=1
'''

'''
4
4 3 
4 3 2 
4 3 2 1 

n = int(input("Enter the number of rows: "))
i = n
while(i >= 1):
    j = n
    while(j >= i):
        print(j,end=" ")
        j-=1
    print()
    i-=1
'''

'''
1
0 1 
0 1 0
1 0 1 0 
'''

n = int(input("Enter the number of rows: "))
x = 0
y = 0

i = 1 
while(i <= n):
    if i%2 == 0:
        x = 1
        y = 0
    else:
        x = 0
        y = 1
    
    j = 1
    while(j <= i):
        if j%2 == 0:
            print(x,end=" ")
        else:
            print(y,end=" ")
        j+=1
    print()
    i+=1