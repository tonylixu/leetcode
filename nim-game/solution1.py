# This solution only works at small cases
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 4:
            if self.canWinNim(n-3):
                return True
            if self.canWinNim(n-2):
                return True
            if self.canWinNim(n-1):
                return True
        if n == 4:
            return False
        if n < 4:
            return True
