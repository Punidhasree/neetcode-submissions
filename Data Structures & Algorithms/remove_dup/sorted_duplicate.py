def remove_dup(arr):
    i=0
    for j in range(len(arr)):
        if arr[i]!=arr[j]:
            arr[i+1]=arr[j]
            i+=1
    return i+1
arr=[1,1,2,2,2,3,4]
print(remove_dup(arr))
print(arr)