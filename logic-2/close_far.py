def close_far(a, b, c):
  return (abs(a - c) <= 1 and abs(a - b) > 1 and abs(b - c) > 1) or (abs(a - b) <= 1 and abs(a - c) > 1 and abs(b - c) > 1)
