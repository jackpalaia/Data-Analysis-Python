import re

def file_listing():
  finalList = []
  with open('listing.txt', 'r') as f:
    for line in f:
      matches = re.search(r'[\d+]', line).groups