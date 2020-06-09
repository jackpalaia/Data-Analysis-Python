shape = input('Choose a shape (triangle, rectangle, circle): ')
while (shape != ''):
  if (shape == 'triangle'):
    base = float(input('Give base of triangle: '))
    height = float(input('Give height of triangle: '))
    print(f'The area is {base * height / 2:.6f}')
  elif (shape == 'rectangle'):
    width = float(input('Give width of rectangle: '))
    height = float(input('give height of rectangle: '))
    print(f'The area is {width * height:.6f}')
  elif (shape == 'circle'):
    radius = float(input('Give radius of circle: '))
    print(f'The area is {.5 * radius**2:.6f}')
  else:
    print('unknown shape!')
  shape = input('Choose a shape (triangle, rectangle, circle): ')