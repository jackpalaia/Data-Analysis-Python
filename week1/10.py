def detect_ranges(list1):
  sortedList = sorted(list1)
  finalList = []
  inRange = False
  for i, val in enumerate(sortedList):
    if (i == len(sortedList) - 1):
      break
    if (not inRange):
      if (sortedList[i + 1] == val + 1):
        finalList.append(f'({val}')
        inRange = True
        continue
      else:
        finalList.append(val)
        continue
    else:
      if (sortedList[i + 1] != val + 1):
        finalList.append(f'{val})')
        inRange = False
        continue
  return finalList

list1 = [5,7,3,1,9,6,2]
print(detect_ranges(list1))