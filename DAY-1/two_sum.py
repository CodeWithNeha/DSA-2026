def two_sum(li, target):
    left= 0
    right = len(li)-1
    while left<right:
        sum = li[left]+li[right]
        if sum == target:
            return [left, right]
        if sum < target:
            left +=1
        else:
            right -=1
    return [-1,-1]



print(two_sum([3,4,5,6,9],10))