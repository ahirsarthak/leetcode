# 2221. Find Triangular Sum of an Array


def sum(nums):
    if not nums:
        return 0

    n = len(nums)
    if n == 1:
        return nums[0]

    while n != 1:
        nums = [(nums[i] + nums[i+1]) % 10 for i in range(n-1)]
        n = len(nums)

    return nums[0]
