def round_sum(a, b, c):
  sum = 0
  for num in (a, b, c):
    sum += round_10(num)
  return sum

def round_10(num):
  if num < 10:
    if num < 5: return 0
    return 10
  checker = num % 10
  if checker == 0: return num
  if checker < 5: return num - checker
  return num + (10 - checker)