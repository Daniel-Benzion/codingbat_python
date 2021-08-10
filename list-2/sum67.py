def sum67(nums):
  sum = 0
  ignore = False
  for i, num in enumerate(nums):
    if num == 6:
      ignore = True
      continue
    if ignore == True:
      if num == 7:
        ignore = False
      continue
    sum += num
    ignore = False
  return sum