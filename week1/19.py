def sum_equation(ints):
  if len(ints) == 0:
    return '0 = 0'
  
  intSum = sum(ints)
  strList = [ str(x) for x in ints ]

  str1 = ' + '.join(strList)
  return(''.join([str1, f' = {intSum}']))

print(sum_equation([1,3,6]))