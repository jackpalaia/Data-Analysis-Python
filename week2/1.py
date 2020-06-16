import re

def integers_in_brackets(s):
  list1 = re.findall(r'(\[[\s+-]*\d+[\s+-]*\])+', s)
  list2 = []
  for x in list1:
    y = x.strip(' []+-')
    list2.append(int(y))
  return list2

def main():
  print(integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
  main()