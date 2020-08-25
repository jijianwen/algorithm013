class Solution(object):
    # Time complexity:  O(N)
    # Space complexity: O(N + M), M is the size of characters
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0: return True
        if len(s) % 2 != 0: return False
        dic = {')':'(', '}':'{', ']':'['}

        res = [s[0]]
        for i in len(s[1:]):
            if s[i] in dic:
                if res[-1] != dic[s[i]]:
                    return False
                else:
                    res.pop()
            else:
                res.push(s[i])


        return len(res) == 0

    def isValid(self, s):
        dic = {'{':'}', '(':')', '[':']', '?':'?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False

        return len(stack) == 1
