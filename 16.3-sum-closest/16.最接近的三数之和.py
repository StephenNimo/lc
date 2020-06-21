#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        mindiff = 10000
        nums.sort()
        res = 0
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                diff = abs(target - sum)
                if diff < mindiff:
                    mindiff = diff
                    res = sum
                if target == sum:
                    return sum
                elif sum < target:
                    left += 1
                else:
                    right -= 1                      

        return res
# @lc code=end

