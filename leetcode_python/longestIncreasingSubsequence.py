# Given an unsorted array of integers, find the length of longest increasing subsequence.

# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

# Your algorithm should run in O(n2) complexity.

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return 0
        # res = [1] * len(nums)
        # for i in range(1,len(nums)):
        #     for j in range(0,i):
        #         if nums[j] < nums[i]:
        #             res[i] = max(res[i],res[j]+1)
        # return max(res)


        dp = []
        for i in range(len(nums)):
            print 'i-nums',i,nums[i],dp
            low,high = 0,len(dp)
            while low < high:
                mid = low + (high-low)/2
                if dp[mid] < nums[i]:
                    low = mid + 1
                else:
                    high = mid
            print 'low',low
            if low < len(dp):
                dp[low] = nums[i]
            else:
                dp.append(nums[i])
            print dp
        return len(dp)

s = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
s.lengthOfLIS(nums)