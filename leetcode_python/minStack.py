class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_v = sys.maxint


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.min_v:
            self.stack.append(self.min_v)
            self.min_v = x
        self.stack.append(x)


    def pop(self):
        """
        :rtype: void
        """
        if self.stack[-1] == self.min_v:
            self.stack.pop()
            self.min_v = self.stack.pop()
        else:
            self.stack.pop()
        if len(self.stack) == 0:
            self.min_v = sys.maxint
            

        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_v


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()