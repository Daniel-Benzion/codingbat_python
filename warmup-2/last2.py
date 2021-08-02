def last2(str):
  to_count = str[-2:]
  count = 0
  for i in range(0, len(str) - 2):
    if str[i:i + 2] == to_count: count += 1
  return count
