def find_matching(strings, search):
  indexList = []
  for i, s in enumerate(strings):
    if search in s:
      indexList.append(i)
  return indexList

def main():
  print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
  main()