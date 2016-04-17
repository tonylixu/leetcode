class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        num = num % 9
        if num == 0:
            return 9
        else:
            return num
