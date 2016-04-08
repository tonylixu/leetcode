class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # We only case if n is a multiplier of 4
        if (n%4 == 0):
            return False
        else:
            return True
