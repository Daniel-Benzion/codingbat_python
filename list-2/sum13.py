def sum13(nums):
  sum = 0
  before = False
    
  for i, num in enumerate(nums):
    if num == 13:
      before = True
      continue
    if before == True:
      before = False
      continue
    sum += num
    before = False
  return sum