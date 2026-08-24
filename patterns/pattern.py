def pattern1(n):
    for i in range(n):
        for j in range(n):
            print('*',end=' ')
        print()


    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        print()

n=5
pattern1(n)
