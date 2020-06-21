#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = list(set(nums))
        for i in range(len(result)):
            nums[i] = result[i]
        for i in range(len(nums) - len(result)):
            nums.pop()
        nums.sort()
        return len(result)
# @lc code=end

