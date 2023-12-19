#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.28%)
# Likes:    21032
# Dislikes: 1338
# Total Accepted:    3.6M
# Total Submissions: 8.9M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para_hash = {
            ")":"(",
            "}":"{",
            "]":"[",
        }

        for w in s:
            # Check stack[0] checks for chrono order
            if stack and stack[0]==para_hash[w]:

                stack.pop[w]
            
            else:
                stack.append(w)
                
        
        return  True if stack else False


sol = Solution

                

print(sol.isValid("()"))

        
# @lc code=end

