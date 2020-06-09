import math

def quad_form(a, b, c, sign):
  if (sign == '+'):
    return (-b + math.sqrt(b**2 - (4 * a * c))) / 2 * a
  else:
    return (-b - math.sqrt(b**2 - (4 * a * c))) / 2 * a

def solve_quadratic(a, b, c):
  return (quad_form(a, b, c, '+'), quad_form(a, b, c, '-'))
  
def main():
  print(solve_quadratic(1, 2, 1))


if __name__ == '__main__':
  main()