# There is a fence with n posts, each post can be painted with one of the k colors.

# You have to paint all the posts such that no more than two adjacent fence posts have the same color.

# Return the total number of ways you can paint the fence.

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0 or k == 0:
            return 0
        if n == 1:
            return k
        same = [0]*n # same[i] records num of ways at post[i] if the color is same as post[i-1]
        diff = [0]*n # diff[i] records num of ways at post[i] if the color is different from post[i-1]
        same[0],diff[0] = k,k
        same[1],diff[1] = k,k*(k-1)
        for i in range(2,n):
            same[i] = diff[i-1]
            diff[i] = (diff[i-1]+same[i-1])*(k-1)
        return same[n-1]+diff[n-1]