import sys
import random
i=random.randint(-10,10)
if i >= 0:
    sys.stdout.write("Got a positive integer.\n")
else:
    sys.stderr.write("Got a negative integer.\n")