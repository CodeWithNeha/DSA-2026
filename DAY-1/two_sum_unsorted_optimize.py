# Hashmap 
def two_sum(li, target):
    seen = {}
    for i,nums in enumerate(li):
        need = target - nums
        if need in seen:
            return [seen[need], i]
        seen[nums] = i
    return [-1,-1]



print(two_sum([2,7,11,15], 9))