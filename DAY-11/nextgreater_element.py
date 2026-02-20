def nextGreaterElement(nums1, nums2):
    stack = []
    nge_map = {}

    # Step 1: Build next greater map for nums2
    for num in nums2:
        while stack and num > stack[-1]:
            smaller = stack.pop()
            nge_map[smaller] = num
        stack.append(num)

    # Remaining elements have no next greater
    while stack:
        nge_map[stack.pop()] = -1

    # Step 2: Build result for nums1
    return [nge_map[num] for num in nums1]

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))