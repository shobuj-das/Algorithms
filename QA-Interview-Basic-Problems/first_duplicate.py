# ============================================================
# Day 14 - Find the First Duplicate Element
#
# Difficulty:
# Easy → Medium
#
# Pattern:
# Hashing (later)
#
# Today:
# Solve WITHOUT using:
# - set
# - dict
# - collections
#
# You may use:
# - list
# - loops
# - if
# - while
# - class
# - object
# - try/except
#
# ------------------------------------------------------------
#
# Problem Statement
#
# Given an integer array,
# return the FIRST element that appears more than once.
#
# "First" means the duplicate whose SECOND occurrence
# appears first while scanning from left to right.
#
# Return None if there is no duplicate.
#
# ------------------------------------------------------------
#
# Example 1
#
# Input:
# [2,5,1,2,3,5,1]
#
# Output:
# 2
#
#
# Explanation
#
# Read left to right
#
# 2
# 5
# 1
# 2  <-- duplicate found first
#
#
# ------------------------------------------------------------
#
# Example 2
#
# Input
#
# [1,2,3,4]
#
# Output
#
# None
#
#
# ------------------------------------------------------------
#
# Example 3
#
# Input
#
# [5,5,1,2]
#
# Output
#
# 5
#
#
# ------------------------------------------------------------
#
# Create the following class
#
#
# class DuplicateFinder:
#
#     def find_first_duplicate(self, numbers):
#         pass
#
#
# ------------------------------------------------------------
#
# Required Test Cases
#
# []
#
# [1]
#
# [1,2,3]
#
# [1,1]
#
# [2,5,1,2,3,5,1]
#
# [5,5,5]
#
# [10,20,30,40]
#
# [-1,-2,-1]
#
# [1,2,3,2,1]
#
# [7,8,9,7]
#
#
# ------------------------------------------------------------
#
# Bonus Challenge (Optional)
#
# Return BOTH
#
# duplicate value
#
# and
#
# duplicate index
#
# Example
#
# Input
#
# [2,5,1,2,3]
#
# Output
#
# Value = 2
# Index = 3
#
#
# ============================================================


class Find_Duplicate:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_first_duplicate(self):
        if not self.numbers:
            return None
        
        for x in range(len(self.numbers)-1):
            for y in range(x+1, len(self.numbers)):
                if self.numbers[x] == self.numbers[y]:
                    return self.numbers[x]
                
        return None

# ---- this will find the first duplicate occurance in the list

class DuplicateFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_first_occurance_duplicate(self):
        if not self.numbers:
            return None
        
        track = set()
        for item in self.numbers:
            if item in track:
                return item
            track.add(item)
        return None
    
        

if __name__=='__main__':
    obj = Find_Duplicate([2,5,1,2,3,5,1])
    print(obj.find_first_duplicate())

    obj1 = Find_Duplicate([1,2,3,4,4])
    print(obj1.find_first_duplicate())

    obj3 = Find_Duplicate([])
    print(obj3.find_first_duplicate())

    obj4 = Find_Duplicate([1])
    print(obj4.find_first_duplicate())

    obj5 = Find_Duplicate([-1,-2,-1])
    print(obj5.find_first_duplicate())

    obj6 = Find_Duplicate([4,4,4,4])
    print(obj6.find_first_duplicate())

    dup = DuplicateFinder([1,2,3,2,1])
    print(dup.find_first_occurance_duplicate())