from collections import defaultdict
def group_anagrams(strs):
    group = defaultdict(list)
    for c in strs:
        count = [0]*26
        for ele in c:
            count[ord(ele)-ord('a')] +=1
        # print(tuple(count))
        group[tuple(count)].append(c)

    return list(group.values())


print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))