# prints all combinations of dice rolls that add to 5
for i in range(1, 7):
  for j in range(1, 7):
    if (i + j == 5):
      print(f'({i},{j})')