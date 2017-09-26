class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        map = {}
        for i in range(length):
            map[nums[i]] = i
            i = i + 1
        print map
        for i in range(length):
            complement = target - nums[i]
            # If a list contains two same integers and the target is happen to
            # be the sum of two same integers
            # for exmaple, [2, 5, 5, 9], target is 10
            # map is {2:0, 5:1, 5:2, 9:3}
            # When i is 1, complement is 10 - 5 which is 5
            # and 5 is definitely in the list
            if map.has_key(complement) and map[complement] is not i:
                return [i, map[complement]]
            i = i + 1
