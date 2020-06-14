def positive_list(numList):
  return list(filter(lambda x : x > 0, numList))

print(positive_list([2,4,0,-1,-2,0,-4]))