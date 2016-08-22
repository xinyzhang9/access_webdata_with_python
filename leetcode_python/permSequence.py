class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def reverse(res,i,j):
            while i<=j:
                res[i],res[j] = res[j],res[i]
                i+=1
                j-=1
                
        def nextPerm(res):
            right = n-1
            while res[right] <= res[right-1] and right-1 >=0:
                right -= 1
            if right == 0:
                return range(1,n+1)
            pivot = right - 1
            rightmost = 0
            for i in reversed(range(pivot,n)):
                if res[i] > res[pivot]:
                    rightmost = i
                    break
            res[pivot],res[rightmost] = res[rightmost],res[pivot]
            reverse(res,pivot+1,n-1)
            print res
            return res

        def fact(n):
            res = 1
            for i in range(1,n+1):
                res*=i
            print res
            return res
        
        res = range(1,n+1)
        for i in range(k % fact(n)-1 + fact(n)):
            res = nextPerm(res)
        return ''.join(str(e) for e in res)

s = Solution()
print s.getPermutation(3,5)