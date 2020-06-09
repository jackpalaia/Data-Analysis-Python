def triple(x):
  '''multiplies parameter by three'''
  return x*3

def square(x):
  '''squares parameter'''
  return x**2

def main():
  for x in range(1, 11):
    if (square(x) <= triple(x)):
      print(f'triple({x})=={triple(x)} square({x})=={square(x)}')
    else:
      break

if __name__ == '__main__':
  main()