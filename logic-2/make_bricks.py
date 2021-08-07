def make_bricks(small, big, goal):
  if goal > ((big * 5) + small): return False
  return goal % 5 <= small
