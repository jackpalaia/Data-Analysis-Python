def reverse_dictionary(d):
  newDict = {}
  for k, v in d.items():
    for val in v:
      if val in newDict.keys():
        newDict[val].append(k)
        continue
      newDict[val] = [k]
  return newDict

def main():
  d = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
  print(reverse_dictionary(d))

if __name__ == "__main__":
  main()