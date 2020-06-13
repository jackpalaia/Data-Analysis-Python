def interleave(*lists):
  list1 = list(zip(lists[0], lists[1]))
  finalList = []
  for group in list1:
    for x in group:
      finalList.append(x)
  return finalList

def main():
  list1 = [1,2,3,4]
  list2 = ['one', 'two', 'three', 'four']
  print(interleave(list1, list2))

if __name__ == "__main__":
  main()