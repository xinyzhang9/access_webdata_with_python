class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        # sort envelopes by width, if same width, larger height first
        nums = sorted(envelopes,cmp=lambda x,y:x[0]-y[0] if x[0] != y[0] else y[1]-x[1])
        size = len(nums)
        dp = []
        for i in range(size):
            low,high = 0, len(dp)-1
            # print 'low','high',low,high
            while low <= high:
                # print 'low','high',low,high
                mid = low + (high-low)/2
                if dp[mid][1] < nums[i][1]:
                    low = mid + 1
                else:
                    high = mid - 1
            if low < len(dp):
                dp[low] = nums[i]
            else:
                dp.append(nums[i])
            # print 'dp',dp
        return len(dp)
                
s = Solution()
envelopes = [(4,5),(4,6),(6,7),(2,3),(1,1)]
s.maxEnvelopes(envelopes)