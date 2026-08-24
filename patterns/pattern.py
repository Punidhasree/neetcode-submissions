def pattern1(n):
    for i in range(n):
        for j in range(n):
            print('*',end=' ')
        print()

#pattern2
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        print()
#pattern3
    for i in range(n):
            for j in range(i+1):
                print(i+1,end=' ')
            print()
 #pattern4   
    for i in range(n):
        
        for j in range(i+1):
            print(j+1,end=' ')
                
        print()
#pattern5
    for i in range(n):
        for j in range(n-i):
            print("*",end=' ')
        print()
#pattern6
    for i in range(n):
        for j in range(n-i):
            print(j+1,end=' ')
        print()
#pattern7   
    for i in range(n):
        for j in range(n-i):
            print(" ",end=' ')
        for _ in range(2*i+1):
            print("*",end=' ')
        for _ in range(n-i):
            print(" ",end=' ')
        print()
#pattern8
    for i in range(n):
        for j in range(i):
            print(" ",end=' ')
        for _ in range(2*(n-i-1)+1):
            print("*",end=' ')
        for _ in range(i):
            print(" ",end=' ')
        print()

    


n=5

pattern1(n)
