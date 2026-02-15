def longest_consecutive(arr):
    longest = 0
    num_set = set(arr)
    for n in num_set:
        if n-1 not in num_set:
            length = 1
            while n+length in num_set:
                length+=1
            longest = max(length, longest)
    return longest

print(longest_consecutive([100,4,200,1,3,2]))
