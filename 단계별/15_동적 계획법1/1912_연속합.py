import sys

# 방법1: 메모이제이션(하향식)
def sub_sum_1(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1] if nums[i-1] > 0 else 0

    return max(nums)

# 방법2: 카데인 알고리즘
def sub_sum_2(nums):
    maxsum = -sys.maxsize
    cursum = 0
    for num in nums:
        cursum = max(num, cursum+num)
        maxsum = max(maxsum, cursum)

    return maxsum

# 입력
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

print(sub_sum_1(nums))
print(sub_sum_2(nums))