#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (43.24%)
# Total Accepted:    1.7M
# Total Submissions: 3.9M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
# 
# 
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #tmp_nums = nums[:]
        #for nums_index, num in enumerate(nums):
        #    for tmp_index, tmp_num in enumerate(tmp_nums):
        #        result = num + tmp_num
        #        if result==target and nums_index != tmp_index:
        #            return [nums_index, tmp_index]
        buff_dic = {}
        for i in range(len(nums)):
            if nums[i] in buff_dic:
                return [buff_dic[nums[i]], i]  # buff_dic
            else:
                buff_dic[target - nums[i]] = i

