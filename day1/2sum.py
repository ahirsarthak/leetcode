

def twoSum(nums, target):

    seen = {}

    for i, value in enumerate(nums):
        current = target - nums[i]
        if current in seen:
            return [seen[current], i]
        else:
            return seen[value]
