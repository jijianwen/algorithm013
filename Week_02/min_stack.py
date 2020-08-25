# https://leetcode.com/problems/min-stack
class MinStack(object):
    # Time complexity:  O(1)
    # Space complexity: O(n)
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [sys.float_info.max]


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))


    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
