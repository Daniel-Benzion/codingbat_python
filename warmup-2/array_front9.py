def array_front9(nums):
  if len(nums) < 4: return nums[0:len(nums)].count(9) > 0
  return nums[0:4].count(9) > 0