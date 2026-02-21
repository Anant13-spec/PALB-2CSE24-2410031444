def arraymedian(arr):
    n = len(arr)
    arr.sort()
    if n%2 == 1:
        return arr[n//2]
    else:
        return (arr[n//2-1]+arr[n//2])/2

print(arraymedian([8,1,2,6,0,9,6,7,4,4,9,9,2,7,1,0,9,9,5,5,9,6,9,0,9,2,6,4,1,4,8,7,5,5,8,9,2,2,9,8]))
