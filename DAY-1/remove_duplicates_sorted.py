def remove_duplicates(li):
    if not li:
        return 0
    slow = 0
    for fast in range(1, len(li)):
        if li[fast]!=li[slow]:
            slow+=1
            li[slow]=li[fast]
    return slow+1

arr = [2,2,3,4,4]
le = (remove_duplicates(arr))
for l in range(0, le):
    print(arr[l], end=" ")
