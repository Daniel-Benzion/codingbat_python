def near_ten(num):
  if num < 10: num_get = num
  else: num_get = num % 10
  return num_get in [0, 1, 2, 8, 9]