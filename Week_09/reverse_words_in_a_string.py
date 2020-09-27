class Solution(object):
    # Time complexity:  O(N)
    # Space complexity: O(N)
    def trim_spaces(self, s):
        l, r = 0, len(s) - 1
        while l <= r and s[l] == ' ':
            l += 1
        while l <= r and s[r] == ' ':
            r -=1

        lst = []
        while l <= r:
            if s[l] != ' ':
                lst.append(s[l])
            elif lst[-1] != ' ':
                lst.append(s[l])
            l += 1

        return lst

    def reverse(self, lst, l, r):
        while l < r:
            lst[l], lst[r] = lst[r], lst[l]
            l, r = l + 1, r - 1

    def reverse_each_word(self, lst):
        n = len(lst)
        start = end = 0

        while start < n:
            while end < n and lst[end] != ' ':
                end += 1
            self.reverse(lst, start, end-1)
            start = end + 1
            end += 1

    def reverseWords(self, s):
        lst = self.trim_spaces(s)
        self.reverse(lst, 0, len(lst) - 1)
        self.reverse_each_word(lst)
        return ''.join(lst)
