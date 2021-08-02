def string_splosion(str):
  list = []
  for i in range(1, len(str) + 1):
    list.append(str[0:i])
  return "".join(val for val in list)