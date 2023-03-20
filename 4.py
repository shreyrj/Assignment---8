class TwoSum:
def find_indices(self, numbers, target):
"""
Finds a pair of indices whose elements' sum equals the target.
:param numbers: a list of integers
:param target: an integer
:return: a tuple of indices (i, j) such that numbers[i] + numbers[j] = target
"""
seen = {}
for i, num in enumerate(numbers):
complement = target - num
if complement in seen:
return seen[complement], i
seen[num] = i
return None