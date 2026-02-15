def subarraySum( nums, k):
        curr_sum = 0
        count = 0
        mp = {0:1}
        for x in nums:
            curr_sum+=x
            if curr_sum-k in mp:
                count += mp[curr_sum-k]
            mp[curr_sum] = mp.get(curr_sum,0)+1
        return count


nums = [1,1,1]
k = 2
print(subarraySum(nums,k))