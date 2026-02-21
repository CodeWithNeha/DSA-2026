def longestBalancedSubstring(s):
    n = len(s)
    ans = 0

    for i in range(n):
        count = {'a': 0, 'b': 0, 'c': 0}
        distinct = 0

        for j in range(i, n):
            ch = s[j]
            if count[ch] == 0:
                distinct += 1
            count[ch] += 1

            # collect frequencies of chars that appear
            freqs = [count[x] for x in count if count[x] > 0]

            if max(freqs) == min(freqs):
                ans = max(ans, j - i + 1)

    return ans


print(longestBalancedSubstring("abbac"))