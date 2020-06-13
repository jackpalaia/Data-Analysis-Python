def distinct_characters(strings):
  d = dict()
  for string in strings:
    d[string] = len(set(string))
  return d

print(distinct_characters(["check", "look", "try", "pop"]))