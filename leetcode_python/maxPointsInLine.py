# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 3:
            return len(points)
        res = -1
        for i in range(len(points)):
            slope = {'inf':0}
            samePoints = 1
            for j in range(len(points)):
                if i == j:
                    continue
                elif points[i].x == points[j].x and points[i].y != points[j].y:
                    slope['inf'] += 1
                elif points[i].x == points[j].x and points[i].y == points[j].y:
                    samePoints += 1
                elif points[i].x != points[j].x:
                    k = 1.0*(points[j].y-points[i].y)/(points[j].x-points[i].x)
                    if k not in slope:
                        slope[k] = 1
                    else:
                        slope[k] += 1
            print slope,samePoints
            res = max(res,max(slope.values())+samePoints)
        return res
                    

s = Solution()
points = [Point(0,0),Point(1,1),Point(1,-1)]
s.maxPoints(points)
                    