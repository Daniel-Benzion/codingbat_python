def no_teen_sum(a, b, c):
  sum = 0
  for num in (a, b, c):
    sum += fix_teen(num)
  return sum
  
def fix_teen(n):
  if n in (13, 14, 17, 18, 19): return 0
  return n