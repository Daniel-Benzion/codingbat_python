def make_chocolate(small, big, goal):
  if goal > (big * 5): result = goal - (big * 5)
  else: result = goal % 5
  if small >= result: return result
  return -1
