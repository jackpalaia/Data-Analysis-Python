def merge(l1, l2):
  '''Merges two already sorted lists together so that the final
  merged list is also in sorted order.'''
  count1 = 0
  count2 = 0
  finalList = []
  for i in range(len(l1) + len(l2)):
    # if length of either list is 0
    if (len(l1) == 0):
      return l2
    if(len(l2) == 0):
      return l1

    if (l1[count1] <= l2[count2]):
      finalList.append(l1[count1])
      count1 += 1
    elif (l1[count1] >= l2[count2]):
      finalList.append(l2[count2])
      count2 += 1
    if (count1 == len(l1)):
      finalList.extend(l2[count2:])
      break
    if (count2 == len(l2)):
      finalList.extend(l1[count1:])
      break
  return finalList

def main():
  list1 = [2]
  list2 = [1,2,3,4,5]
  print(merge(list1, list2))

if (__name__ == '__main__'):
  main()