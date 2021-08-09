def end_other(a, b):
  a1 = a.lower()
  b1 = b.lower()
  if len(a) == len(b): return a1 == b1
  if len(a) < len(b): return b1[(len(a) * -1):] == a1
  return a1[(len(b) * -1):] == b1