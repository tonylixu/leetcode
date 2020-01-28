class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr_dict = {}
        for x in arr:
            if x in arr_dict:
                arr_dict[x] += 1
            else:
                arr_dict[x] = 1
        if len(set(arr_dict.values())) != len(arr_dict.values()):
            return False
        else:
            return True
