class Solution(object):
    # Time complexity: O(n), time to iterate list: bills
    # Spance complexity: O(1)
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five, ten = 0, 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0: return False
                five -= 1
                ten += 1
            else:
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
