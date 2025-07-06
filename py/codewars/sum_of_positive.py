def positive_sum (arr):
    return sum(x for x in arr if x>0)
nums = input()
arr = list(map(int, nums.split()))
print(positive_sum(arr))