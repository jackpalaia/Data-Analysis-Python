def two_dice():
  pairs = [ (a, b) for a in range(1, 7) for b in range(1, 7) if a + b == 5]
  for pair in pairs:
    print(pair)

def main():
  two_dice()

if __name__ == "__main__":
  main()