def compression(strs):
    write = 0
    i = 0
    while i<len(strs):
        char = strs[i]
        count = 0
        while i<len(strs) and strs[i] == char:
            i+=1
            count+=1
        strs[write] = char
        write +=1
        if count>1:
            for c in str(count):
                strs[write] = c
                write+=1
    return write

print(compression(["a","a","b","b","c","c","c"]))
    
