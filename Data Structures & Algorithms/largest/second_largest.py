def LE(arr):
    Largest=arr[0]
    sec_Lar=float('-inf')
    for num in arr:
        if num>Largest:
            sec_Lar=Largest
            Largest=num
            if num>sec_Lar and num!=Largest:
                sec_Lar=num

    return sec_Lar
arr=[2,4,6,3,5]
print(LE(arr))