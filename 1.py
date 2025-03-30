nums = list(map(int, input().split(",")))
def second_largest(nums):
    if len(nums) < 2:
        return -1 
    nums = list(set(nums))  # Remove duplicates
    nums.sort()
    if len(nums) > 1:
        return nums[-2]
    else:
        return-1 
print(second_largest(nums))  
