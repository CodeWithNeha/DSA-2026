def reverse_words(strs):
    li = strs.split()
    return " ".join(reversed(li))

print(reverse_words("the sky in blue"))