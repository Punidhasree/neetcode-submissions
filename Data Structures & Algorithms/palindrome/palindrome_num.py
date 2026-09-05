num=121
ori=num
rev=0
while num>0:
    ld=num%10
    rev=(rev*10)+ld
    num//=10
if rev==ori:
    print("Palindrome")
else:
    print("Not a palindrome")
