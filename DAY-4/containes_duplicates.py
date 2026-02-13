def contain_duplicates(arr):
    seen = set()
    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False

print(contain_duplicates([1,2,3,1]))