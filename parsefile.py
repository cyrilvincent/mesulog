import csv

with open("mesures.csv") as f:
    reader = csv.DictReader(f)
    diff = [abs(float(row["VM"]) - float(row["VT"])) for row in reader]
    print(list(diff))

def add(a,b):
    return a+b

import unittest
class MyTests(unittest.TestCase):

    def testFirst(self):
        x = add(1,2)
        self.assertEqual(3, x)

unittest.main()




