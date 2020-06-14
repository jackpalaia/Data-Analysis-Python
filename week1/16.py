def transform(s1, s2):
  return list(map(lambda t : t[0] * t[1], list(zip(list(map(int, s1.split())), list(map(int, s2.split()))))))

print(transform('1 5 3', '4 6 -2'))