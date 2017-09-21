class Solutions(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, nums.length()):
            for j in range(i+1, nums.length()):
                if nums[i] + nums[j] == target:
                    return [i, j]
                else:
                    j = j + 1
            else:
                i = i + 1
