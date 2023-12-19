#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (41.05%)
# Likes:    16220
# Dislikes: 4269
# Total Accepted:    2.8M
# Total Submissions: 6.7M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# 
# Example 1:
# 
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        if len(strs) == 0:
            return lcp
        
        # longest length
        min_str_len = len(strs[0])

        # find shortest string
        for s in strs:
            min_str_len = min(min_str_len, len(s))

        # loop through each character
        for i in range(0, min_str_len):

            # get current character of first string
            current = strs[0][i]

            # check if current character is presented in other strings
            for j in range(0, len(strs)):
                if current != strs[j][i]:
                    return lcp
            lcp += current
        return lcp


        
# @lc code=end


