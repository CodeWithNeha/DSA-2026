def contain_duplicates(arr, k):
    seen = set()
    for x, num in enumerate(arr):
        if num in seen:
            return True
        seen.add(num)
        if len(seen)>k:
            seen.remove(arr[x-k])
    return False

print(contain_duplicates([1,2,3,1], 3))