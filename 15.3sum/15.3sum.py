#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        slen = len(nums)
        if slen<3:
            return []
        nums.sort()
        ans = []
        i=0
        while i<slen:
            front, back = i+1, slen-1
            total = -nums[i]
            while front < back:
                sum = nums[front] + nums[back]
                if sum<total:
                    front+=1
                elif sum>total:
                    back-=1
                else:
                    tmp = [nums[i],nums[front],nums[back]]
                    ans.append(tmp)
                    while front < back and nums[front]==tmp[1]:
                        front+=1
                    while front < back and nums[back] ==tmp[2]:
                        back-=1
            i+=1
            while i<slen and nums[i-1]==nums[i]:
                i+=1
        return ans
# @lc code=end

