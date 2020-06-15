'''This module contains a hypotenuse and area method for a triangle.'''

__version__ = '1.0'
__author__ = 'Jack Palaia'

def hypotenuse(l1, l2):
  '''Calculates the length of a hypotenuse given two other sides of triangle'''
  return (l1**2 + l2**2)**.5

def area(s1, s2):
  '''Calculates area of right triangle given two non-hypotenuse sides'''
  return .5 * s1 * s2