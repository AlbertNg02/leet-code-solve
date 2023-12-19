#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (63.52%)
# Likes:    11071
# Dislikes: 349
# Total Accepted:    2.9M
# Total Submissions: 4.5M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_store = {}
        t_store = {}

        for word in s:
            s_store[word] = 1 + s_store.get(word, 0)
        for word in t:
            t_store[word] = 1 + t_store.get(word, 0)
        for c in s_store:
            if s_store[c] != t_store.get(c,0):
                return False
        
        return True
        


        
            
            

        
# @lc code=end

