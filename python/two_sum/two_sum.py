#!/usr/bin/env python3

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    while i < len(nums):
        currentValue = nums[i]
        xs = nums[i+1:]
        x = 0
        while x < len(xs):
            if currentValue + xs[x] == target:
                return [i, x + i + 1]
            x += 1
        i += 1


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print('{0}'.format(twoSum(nums, target)))
