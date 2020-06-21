#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        for i in range(len(nums)):
            if val != nums[i]:
                tmp.append(nums[i])
                nums[len(tmp) - 1] = nums[i]
        
        return len(tmp)
# @lc code=end

