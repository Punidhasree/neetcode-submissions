s='Hello'
rev=''
for ch in s:
    rev=ch+rev
if rev==s:
    print("Palindrome")
else:
    print("Not a palindrome")