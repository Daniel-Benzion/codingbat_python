def count_evens(nums):
  count = 0
  for i, num in enumerate(nums):
    if num % 2 == 0: count += 1
  return count