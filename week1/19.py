def sum_equation(ints):
  if len(ints) == 0:
    return '0 = 0'
  intSum = sum(ints)
  return ''.join([' + '.join(str(ints)).strip(' + '), f' = {intSum}'])

print(sum_equation([1,3,6]))