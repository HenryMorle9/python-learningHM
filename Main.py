# ==============================
# PYTHON ARRAY PRACTICE SET 1
# ==============================

# 1️⃣ FIND MAXIMUM
# Given a list of integers, return the largest number.
# Do NOT use max().
#
# Example:
# Input:  [3, 7, 2, 9, 4]
# Output: 9

def find_max(nums):
    largest = nums[0]
    for num in nums:
        if(num>largest):
            largest = num
    return(largest)

def find_maxOtherWay(nums):
    largest = nums[0]
    for num in range(1, len(nums)):
        if nums[num]>largest:
            largest = nums[num]
    return largest



# 2️⃣ SUM OF ELEMENTS
# Return the total sum of all elements in a list.
# Do NOT use sum().
#
# Example:
# Input:  [1, 2, 3, 4]
# Output: 10

def find_sum(nums):
    result = 0
    for i in range(len(nums)):
        result = result + nums[i]
        #result+=nums
    return result



# 3️⃣ COUNT EVEN NUMBERS
# Return how many even numbers are in a list.
#
# Example:
# Input:  [1, 2, 4, 7, 8]
# Output: 3

def count_evens(nums):
    evenAmount = []
    for num in nums:
        if num % 2==0:
            evenAmount.append(num)
    return len(evenAmount)

#simpler

def count_evens(nums):
    count = 0
    for num in nums:
        if(num%2==0):
            count+=1
    return count



# 4️⃣ SECOND LARGEST NUMBER
# Return the second largest number in a list.
# Try to do it in ONE PASS.
#
# Example:
# Input:  [10, 5, 8, 20]
# Output: 10

def second_largest(nums):
    largest= nums[0]
    prevLargest= nums[0]
    for i in range(len(nums)):
        if nums[i] > largest:
            prevLargest = largest
            largest = nums[i]
        elif nums[i] > prevLargest and nums[i] < largest:
            prevLargest = nums[i]
    return prevLargest
        
        



# 5️⃣ REVERSE ARRAY
# Return a new list that is reversed.
# Do NOT use reverse() or slicing [::-1]
#
# Example:
# Input:  [1, 2, 3]
# Output: [3, 2, 1]

def reverse_array(nums):
    revList = []
    reversePos = 1
    for num in nums:
        revList.insert(0, num)
    return revList




# 6️⃣ CHECK IF SORTED
# Return True if the list is sorted in ascending order.
# Otherwise return False.
#
# Example:
# [1, 2, 3, 5] → True
# [1, 4, 2] → False

def is_sorted(nums):
    prev = nums[0]
    for num in nums:
        if num < prev:
            return False
        prev = num
    return True
   
            



# 7️⃣ REMOVE DUPLICATES (KEEP ORDER)
# Return a new list with duplicates removed,
# but keep the original order.
#
# Example:
# Input:  [1, 2, 2, 3, 1]
# Output: [1, 2, 3]

def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result

# ==============================
# SET PRACTICE PROBLEMS
# ==============================


# 1️⃣ CONTAINS DUPLICATE
# Return True if any value appears at least twice.
# Return False if all elements are unique.
#
# Example:
# [1, 2, 3, 1] → True
# [1, 2, 3, 4] → False

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False




# 9️⃣ TWO SUM
# Given a list and a target,
# return the indices of two numbers that add up to the target.
# You may assume exactly one solution exists.
#
# Example:
# nums = [2, 7, 11, 15]
# target = 9
# Output: [0, 1]

def two_sum(nums, target):
    seen = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], index]

        seen[num] = index