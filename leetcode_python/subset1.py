class Solution(object):
    def subset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        # def backtrack(nums,res,tmp,start):
        #     res.append(list(tmp))
        #     print res
        #     for i in range(start,len(nums)):
        #         tmp.append(nums[i])
        #         backtrack(nums,res,tmp,i+1)
        #         tmp.pop()

        # backtrack(nums,res,[],0)
        # return res
        l = 1
        for n in nums:
            print res
            for i in range(len(res)-l,len(res)):
                res.append(res[i]+[n])
            l = len(res)
            
        print res
        return res

s = Solution()
s.subset([1,2,3])

        