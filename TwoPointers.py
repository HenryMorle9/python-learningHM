# ============================================================
# TWO POINTERS TRAINING FILE
# Learning order: easiest -> harder
# Language: Python
#
# How to use this file:
# 1. Read the problem comment
# 2. Solve it yourself under the method
# 3. After solving, write:
#    - Time Complexity
#    - Space Complexity
#    - Pattern Used
#    - Key Insight
# 4. Then move to the next problem
# ============================================================


# ------------------------------------------------------------
# 1) Reverse an Array
# ------------------------------------------------------------
# Difficulty: Very Easy
#
# Problem:
# Given an array of integers, reverse the array in place.
#
# Example:
# Input:  [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
#
# Goal:
# Learn the most basic opposite-end two pointer movement.
#
# Pattern:
# - One pointer starts at the left
# - One pointer starts at the right
# - Swap values
# - Move both pointers inward
#
# What to focus on:
# - Pointer setup
# - Pointer movement
# - When to stop
# ------------------------------------------------------------
def reverse_array(nums):
    left = 0
    right = len(nums-1)
    while left <= right:  
        nums[left], nums[right] = nums[right], nums[left]
        
        left += 1
        right -+1
    return nums

# ------------------------------------------------------------
# String Palindrome Check
# ------------------------------------------------------------
# Difficulty: Very Easy
#
# Problem:
# Given a string, determine whether it is a palindrome.
#
# A palindrome reads the same forwards and backwards.
#
# Example:
# Input: "racecar"
# Output: True
#
# Example:
# Input: "hello"
# Output: False
#
# Goal:
# Practice comparing characters from both ends of a string
# using the two pointer technique.
#
# Pattern:
# - One pointer starts at the beginning of the string
# - One pointer starts at the end of the string
# - Compare characters
# - If they differ → return False
# - If pointers meet without mismatches → return True
#
# What to focus on:
# - Understanding pointer movement
# - Stopping condition
# - Comparing characters instead of swapping

def is_palindrome_string(s):
    left = 0
    right = len(s)-1
    
    while left < right:
        
        if s[right] !=s[left]:
            return False
        left +=1; right -=1
    return True


# ------------------------------------------------------------
# 2) Check if Array is a Palindrome
# ------------------------------------------------------------
# Difficulty: Very Easy
#
# Problem:
# Given an array, determine whether it reads the same
# forward and backward.
#
# Example:
# Input:  [1, 2, 3, 2, 1]
# Output: True
#
# Example:
# Input:  [1, 2, 3, 4]
# Output: False
#
# Goal:
# Practice comparing values from both ends instead of swapping.
#
# Pattern:
# - One pointer at the start
# - One pointer at the end
# - Compare values
# - If mismatch, return False
# - If all match, return True
#
# What to focus on:
# - Same two pointer structure as reverse
# - Different operation: compare instead of swap
# ------------------------------------------------------------
def is_array_palindrome(nums):
    
    right = len(nums)-1
    left = 0
    
    while left < right:
        if nums[left]!= nums[right]:
            return False
        left += 1
        right -=1
    return True


# ------------------------------------------------------------
# 3) Move Zeros to the End
# ------------------------------------------------------------
# Difficulty: Easy
#
# Problem:
# Given an array, move all zeros to the end while keeping
# the relative order of non-zero elements the same.
#
# Modify the array in place.
#
# Example:
# Input:  [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
#
# Goal:
# Learn the slow/fast pointer pattern.
#
# Pattern:
# - Fast pointer scans every element
# - Slow pointer tracks where the next non-zero should go
#
# What to focus on:
# - Difference between opposite-end pointers and slow/fast pointers
# - In-place overwriting or swapping logic
# ------------------------------------------------------------
def move_zeros(nums):
    
    # scan = 0
    # store = len(nums)-1
    
    # while scan < store:
    #     if nums[scan] == 0:
    #         nums[scan] = nums[store]
    #         nums[store] = 0
    #         store -=1 
    #     scan +=1
    # return nums    

    store = 0
    
    for scan in range(len(nums)):
        
        if scan != 0:
            nums[store] = nums[scan]
            nums[scan] = nums[store]
            store +=1
            
    return nums
        
        


# ------------------------------------------------------------
# 4) Two Sum II (Sorted Array)
# ------------------------------------------------------------
# Difficulty: Easy
#
# Problem:
# You are given a sorted array of integers and a target.
# Return the indices of the two numbers that add up to target.
#
# Assume:
# - The array is sorted in non-decreasing order
# - Exactly one solution exists
# - You must use constant extra space
#
# Example:
# nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
#
# Goal:
# Learn how pointer movement can depend on the current sum.
#
# Pattern:
# - Left pointer at start
# - Right pointer at end
# - If current sum is too small, move left
# - If current sum is too large, move right
#
# What to focus on:
# - Why sorting makes two pointers possible here
# - How to decide which pointer to move
# ------------------------------------------------------------
def two_sum_sorted(nums, target):
    pass


# ------------------------------------------------------------
# 5) Valid Palindrome
# ------------------------------------------------------------
# Difficulty: Easy
#
# Problem:
# Determine whether a string is a palindrome.
#
# Ignore:
# - spaces
# - punctuation
# - case differences
#
# Example:
# Input:  "A man, a plan, a canal: Panama"
# Output: True
#
# Example:
# Input:  "race a car"
# Output: False
#
# Goal:
# Practice two pointers with skipping logic.
#
# Pattern:
# - Pointer at start
# - Pointer at end
# - Skip non-alphanumeric characters
# - Compare lowercase versions of characters
#
# What to focus on:
# - Pointer movement is no longer always symmetrical
# - Sometimes one pointer moves while the other stays
# ------------------------------------------------------------
def is_palindrome(s):
    pass


# ------------------------------------------------------------
# 6) Remove Duplicates from Sorted Array
# ------------------------------------------------------------
# Difficulty: Easy
#
# Problem:
# Given a sorted array, remove duplicates in place so that
# each unique element appears only once.
#
# Return the number of unique elements.
#
# Example:
# Input:  [1, 1, 2]
# Output: 2
# Array becomes [1, 2, _]
#
# Example:
# Input:  [0,0,1,1,1,2,2,3,3,4]
# Output: 5
# Array becomes [0,1,2,3,4,_,_,_,_,_]
#
# Goal:
# Practice read/write style slow/fast pointers.
#
# Pattern:
# - Fast pointer scans through the array
# - Slow pointer writes the next unique value
#
# What to focus on:
# - Difference between reading and writing positions
# - Why the input being sorted matters
# ------------------------------------------------------------
def remove_duplicates(nums):
    pass


# ------------------------------------------------------------
# 7) Squares of a Sorted Array
# ------------------------------------------------------------
# Difficulty: Easy to Medium
#
# Problem:
# Given a sorted array of integers, return an array of the
# squares of each number, also sorted in non-decreasing order.
#
# The input may include negative numbers.
#
# Example:
# Input:  [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]
#
# Goal:
# Learn that the largest value can come from either end.
#
# Pattern:
# - Compare absolute values / squared values at both ends
# - Place the larger square into the back of the result
# - Move the corresponding pointer
#
# What to focus on:
# - Why squaring negatives breaks the original sorted order
# - Why filling from the back is the clean trick
# ------------------------------------------------------------
def sorted_squares(nums):
    pass


# ------------------------------------------------------------
# 8) Container With Most Water
# ------------------------------------------------------------
# Difficulty: Medium
#
# Problem:
# Given an array of heights, choose two lines that together
# form a container holding the maximum amount of water.
#
# The amount of water is:
# min(height[left], height[right]) * (right - left)
#
# Example:
# Input:  [1,8,6,2,5,4,8,3,7]
# Output: 49
#
# Goal:
# Learn the important rule:
# move the pointer pointing to the smaller height.
#
# Pattern:
# - One pointer at the left
# - One pointer at the right
# - Compute area
# - Move the smaller-height pointer inward
#
# What to focus on:
# - Why moving the taller one does not help
# - How the width shrinks each step
# ------------------------------------------------------------
def max_area(height):
    pass


# ------------------------------------------------------------
# 9) 3Sum
# ------------------------------------------------------------
# Difficulty: Medium
#
# Problem:
# Given an integer array nums, return all unique triplets
# [nums[i], nums[j], nums[k]] such that:
#
# nums[i] + nums[j] + nums[k] == 0
#
# The solution set must not contain duplicate triplets.
#
# Example:
# Input:  [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
#
# Goal:
# Learn the common interview move:
# sort + fix one value + run two pointers on the rest.
#
# Pattern:
# - Sort the array
# - Loop through each index as the fixed first number
# - Use two pointers on the remaining right side
# - Skip duplicates carefully
#
# What to focus on:
# - This is not a beginner problem, so do not rush it
# - Duplicate handling matters a lot
# - Understand the structure before trying to code fast
# ------------------------------------------------------------
def three_sum(nums):
    pass


# ------------------------------------------------------------
# BONUS 10) Longest Palindromic Substring
# ------------------------------------------------------------
# Difficulty: Medium
#
# Problem:
# Given a string s, return the longest substring of s that
# is a palindrome.
#
# Example:
# Input:  "babad"
# Output: "bab" or "aba"
#
# Example:
# Input:  "cbbd"
# Output: "bb"
#
# Goal:
# Learn a different two pointer style:
# expand around center.
#
# Pattern:
# - Pick a center
# - Expand outward while characters match
# - Check both odd-length and even-length centers
#
# What to focus on:
# - This is still two pointers, but not start/end
# - Great for understanding pattern flexibility
# ------------------------------------------------------------
def longest_palindrome(s):
    pass


# ============================================================
# OPTIONAL PRACTICE NOTES TEMPLATE
# Copy this under each solution after you finish it.
# ============================================================

# Time Complexity:
# Space Complexity:
# Pattern Used:
# Key Insight:
# Mistake I made:
# What I should remember next time:


# ============================================================
# SUGGESTED STUDY METHOD
# ============================================================
#
# Reverse Array
#   -> do until pointer movement feels obvious
#
# Array Palindrome
#   -> do until comparisons from both ends feel easy
#
# Move Zeros
#   -> do until you understand slow/fast clearly
#
# Two Sum II
#   -> do until you understand why sorting helps
#
# Valid Palindrome
#   -> do until skip logic feels natural
#
# Remove Duplicates
#   -> do until read/write pointer logic clicks
#
# Sorted Squares
#   -> do until "largest can come from either end" clicks
#
# Container With Most Water
#   -> do until you truly understand why you move the shorter side
#
# 3Sum
#   -> do only after the earlier ones feel solid
#
# Longest Palindromic Substring
#   -> bonus pattern: expand around center
#
# ============================================================
# IMPORTANT
# Do not just read these.
# Actually solve them.
# If you get stuck, trace pointer positions on paper like:
#
# nums = [1, 2, 3, 4, 5]
#         L           R
#
# Then update them step by step.
# That is how two pointers starts becoming intuitive.
# ============================================================