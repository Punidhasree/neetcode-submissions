def arm(num):
    length=len(str(num))
    summ=0
    original=num
    while num>0:
        ld=num%10
        summ+=ld**length
        num//=10
    if original==summ:
        return True
    else:
        return False




num=153
print(arm(num))