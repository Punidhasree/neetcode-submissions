def largest_element(arr):
    arr.sort()
    
    return arr[len(arr)-1]
arr=[2,3,5,6,4]
print(largest_element(arr))

def LE(arr):
    Largest=arr[0]
    for num in arr:
        if num>Largest:
            Largest=num
    return Largest
print(LE(arr))