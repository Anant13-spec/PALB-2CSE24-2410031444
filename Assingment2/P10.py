def triplet_sum(arr, target):
    arr.sort()

    for i in range(len(arr)-2):
        l = i+1
        r = len(arr)-1

        while l < r:
            s = arr[i] + arr[l] + arr[r]

            if s == target:
                return True
            elif s < target:
                l += 1
            else:
                r -= 1

    return False


# Test
print(triplet_sum([1,4,45,6,10,8], 13))
