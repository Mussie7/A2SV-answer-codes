count = 0
    nums.sort()
    i = 0
    j = len(nums) - 1
    while j > i:
        addition = nums[i] + nums[j]
        if addition == k:
            count += 1
            i += 1
            j -= 1
        elif addition < k:
            i += 1
        else:
            j -= 1
    return count
