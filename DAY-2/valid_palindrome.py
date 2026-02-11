def valid_palindrome(st):
    left = 0
    right = len(st)-1
    while left<right:
        while left<right and not st[left].isalnum():
            left+=1
        while left<right and not st[right].isalnum():
            right-=1
        if st[left].lower() != st[right].lower():
            return False
        left += 1
        right -=1
    return True

print(valid_palindrome("A man, a plan, a canal: Panama"))