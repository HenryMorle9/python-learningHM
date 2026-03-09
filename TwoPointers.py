
# note:
# Time Complexity:
# Space Complexity:
# Pattern Used:
# Key Insight:

# Two Sum II
# You are given a sorted array of integers and a target value.
# Return the indices of the two numbers such that they add up to the target.
#
# Constraints:
# - The array is sorted in non-decreasing order
# - Exactly one solution exists
# - Use constant extra space
#
# Example:
# nums = [2,7,11,15], target = 9
# Output: [0,1]
#
# Pattern:
# Two pointers from opposite ends.
# If sum too small → move left pointer
# If sum too large → move right pointer

def two_sum_sorted(nums, target):
    pass

# Valid Palindrome
# Determine whether a string is a palindrome.
#
# Ignore:
# - punctuation
# - spaces
# - letter casing
#
# Example:
# "A man, a plan, a canal: Panama" -> True
#
# Pattern:
# Two pointers from both ends.
# Skip non-alphanumeric characters while comparing.

def is_palindrome(s):
    pass

# Remove Duplicates from Sorted Array
# Given a sorted array, remove duplicates in place.
#
# Return the number of unique elements.
#
# Example:
# Input: [1,1,2]
# Output: 2
# Array becomes [1,2,_]
#
# Pattern:
# Fast and slow pointer.
# Fast scans array, slow tracks location of next unique element.

def remove_duplicates(nums):
    pass

# Squares of a Sorted Array
# Given a sorted array that may contain negative numbers,
# return a new array containing the squares of each number
# sorted in non-decreasing order.
#
# Example:
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
#
# Key idea:
# The largest square will come from either end of the array.
#
# Pattern:
# Two pointers at start and end.
# Fill result array from the back.

def sorted_squares(nums):
    pass

# Container With Most Water
# Given an array where each element represents the height
# of a vertical line, find two lines that together form
# the container holding the maximum amount of water.
#
# Water area = min(height[left], height[right]) * width
#
# Example:
# height = [1,8,6,2,5,4,8,3,7]
# Output: 49
#
# Pattern:
# Two pointers from opposite ends.
# Move the pointer with the smaller height.

def max_area(height):
    pass

# 3Sum
# Given an integer array nums, return all unique triplets
# [nums[i], nums[j], nums[k]] such that:
#
# nums[i] + nums[j] + nums[k] == 0
#
# Example:
# nums = [-1,0,1,2,-1,-4]
# Output:
# [[-1,-1,2], [-1,0,1]]
#
# Constraints:
# - No duplicate triplets allowed
#
# Pattern:
# Sort array
# Iterate each element
# Use two pointers to find remaining pair

def three_sum(nums):
    pass

# Longest Palindromic Substring
# Given a string s, return the longest substring that
# is a palindrome.
#
# Example:
# Input: "babad"
# Output: "bab" or "aba"
#
# Pattern:
# Expand around center.
# For each index, check:
# - odd length palindrome
# - even length palindrome

def longest_palindrome(s):
    pass