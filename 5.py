class ThreeSum:
def find_triplets(self, nums):
"""
Finds all triplets in nums that add up to zero.
:param nums: a list of integers
:return: a list of lists of integers, each inner list representing a triplet that adds up to zero
"""
nums.sort()
n = len(nums)
triplets = []
for i in range(n - 2):
if i > 0 and nums[i] == nums[i - 1]:
continue
j, k = i + 1, n - 1
while j < k:
total = nums[i] + nums[j] + nums[k]
if total == 0:
triplets.append([nums[i], nums[j], nums[k]])
j += 1
k -= 1
while j < k and nums[j] == nums[j - 1]:
j += 1
while j < k and nums[k] == nums[k + 1]:
k -= 1
elif total < 0:
j += 1
else:
k -= 1
return triplets