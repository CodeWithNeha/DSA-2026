def nextGreater(nums):
    stack = []
    res = [-1] * len(nums)

    for i in range(len(nums)-1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(nums[i])

    return res

print(nextGreater([1,2,3,4,5]))