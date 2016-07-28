class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        res = 0
        n = len(prices)
        # left[i] records max profit from day[0] to day[i-1], right[i] records max profit after day i
        left,right = [0]*n,[0]*n
        min_v = prices[0]
        # compute left
        for i in range(1,n):
            left[i] = max(left[i-1],prices[i]-min_v)
            min_v = min(min_v,prices[i])
        # compute right
        max_v = prices[n-1]
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1],max_v-prices[i])
            max_v = max(max_v,prices[i])
        # find the max of left[i]+right[i]
        return max(sum(x) for x in zip(left,right))
        
        
s = Solution()

prices = [1,3,2,4]
s.maxProfit(prices)