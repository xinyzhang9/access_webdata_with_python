class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = list(reversed(digits))
        c = 1
        for i in range(len(res)):
            if i==len(res)-1 and c+res[i] == 10:
                res[i] = 0
                res.append(1)
                return list(reversed(res))
            if c+res[i] == 10:
                c = 1
                res[i] = 0
            else:
                c = 0
                res[i] += 1
                break #only plus 1 once! 
            
        return list(reversed(res))
        