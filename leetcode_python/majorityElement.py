# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         dic = dict()
#         for i in range(len(nums)):
#             if nums[i] not in dic:
#                 dic[nums[i]] = 1
#             else:
#                 dic[nums[i]] += 1
#             if dic[nums[i]] > len(nums)/2:
#                     return nums[i]
#         return None


# genius solution

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj = nums[0]
        count = 1
        for i in range(1,len(nums),1):
            if count == 0:
                count += 1
                maj = nums[i]
            elif nums[i] == maj:
                count += 1
            else:
                count -= 1
            # print maj, count
        return maj

s = Solution()
print s.majorityElement([1,1,2,2,2])
