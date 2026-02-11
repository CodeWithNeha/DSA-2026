def two_sum(li, target):
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if li[i]+li[j] == target:
                return [i,j]
    return [-1,-1]

print(two_sum([2,7,11,15], 9))