def interleave(*lists):
  list1 = list(zip(*lists))
  finalList = []
  for group in list1:
    finalList.extend(group)
  return finalList

def main():
  list1 = [1,2,3,4]
  list2 = ['one', 'two', 'three', 'four']
  print(interleave([1,2,3], [20,30,40], ['a', 'b', 'c']))

if __name__ == "__main__":
  main()