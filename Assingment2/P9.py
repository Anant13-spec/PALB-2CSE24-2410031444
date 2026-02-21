def is_subset(a, b):
    a.sort()
    b.sort()

    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            return False

    return j == len(b)


# Test
print(is_subset([11,7,1,13,21,3,7,3], [11,3,7,1,7]))
