def caught_speeding(speed, is_birthday):
  low = 60
  med_start = 61
  med_end = 80
  high = 81
  
  if is_birthday:
    low += 5
    med_start += 5
    med_end += 5
    high += 5
  
  if speed <= low: return 0
  if med_start <= speed <= med_end: return 1
  return 2
  