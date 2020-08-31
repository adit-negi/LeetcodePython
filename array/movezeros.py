count = 0
i = 0
nums = [0, 0, 1]
while i < len(nums):
    if nums[i] == 0:
        nums.pop(i)
        count = count+1
        i = i-1
    i = i+1

print(nums)
