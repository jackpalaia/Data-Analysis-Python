def detect_ranges(list1):
  sortedList = sorted(list1)
  finalList = []
  inRange = False
  rangeTracker = [0, 0]

  for (i, x) in enumerate(sortedList):
    if (i == len(sortedList) - 1):
      if (inRange):
        if (x == sortedList[i - 1] + 1):
          rangeTracker[1] += 1
          finalList.append(tuple(rangeTracker))
          break
        else:
          finalList.append(x)
          break
      else:
        finalList.append(x)
        break
    if (not inRange):
      if (sortedList[i + 1] != x + 1):
        finalList.append(x)
        continue
      else:
        rangeTracker = [x, x + 1]
        inRange = True
        continue
    else:
      if (sortedList[i + 1] == x + 1):
        rangeTracker[1] += 1
        continue
      else:
        rangeTracker[1] += 1
        finalList.append(tuple(rangeTracker))
        inRange = False
        continue
  
  return finalList

list1 = [2,5,4,8,12,6,7,10,13]
print(detect_ranges(list1))