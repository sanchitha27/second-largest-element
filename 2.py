def sec_largest(self, arr):
    n=len(arr)
    if n>2:
        return -1
    first=second=float('-inf')
    for num in arr:
        if num>first:
            second=first
            first=num
        elif num>second and num != first:
            second=num
    if secnd == float('-inf'):
        return -1
    else:
        return second
nums = list(map(int, input().split(",")))
print(second_largest(nums))  
