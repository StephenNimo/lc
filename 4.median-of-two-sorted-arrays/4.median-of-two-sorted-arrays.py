#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_list = nums1 + nums2
        merge_list.sort()
        if(len(merge_list) % 2 ==  0):
            return (merge_list[len(merge_list)//2] + merge_list[len(merge_list)//2 - 1]) / 2
        else:
            return merge_list[len(merge_list)//2]
        
# @lc code=end

