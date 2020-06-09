def length(*t, degree=2):
  '''computes the length of the vector given as parameter. By default,
  the Euclidian distance (degree == 2)'''
  s = 0
  for x in t:
    s += abs(x)**degree
  return s**(1/degree)
print(length(-4, 3))
print(length(-4, 3, degree=3))