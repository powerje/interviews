#!/usr/bin/env python3

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    cached = {}
    for i, num in enumerate(nums):
        checkKey = target - num
        if checkKey in cached:
            return [cached[checkKey], i]
        cached[num] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print('{0}'.format(twoSum(nums, target)))
