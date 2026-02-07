a = [2,3,-8,7,-1,2,3]
currsubarray = a[0]
max_subarray = a[0]
for i in range(1,len(a)):
    currsubarray = max(a[i],currsubarray + a[i])
    max_subarray = max(currsubarray,max_subarray)

print(max_subarray)