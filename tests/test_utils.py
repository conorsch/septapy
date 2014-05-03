import sys
import os
import unittest
sys.path.insert(0, os.path.abspath( os.path.join(os.path.dirname(__file__), '../septapy/') ))
import septapy
import mockdata

class TestUtils(unittest.TestCase):

    def setUp(self):
        # Print out name of method
        sys.stdout.flush()
        sys.stdout.write("\nRunning test '%s'..." % self._testMethodName)
        sys.stdout.flush()

    def testGetKML(self):
        results = septapy.utils.getKML(mockdata.KMLURL)
        self.assertIsInstance(results, list)
        for r in results:
            self.assertIsInstance(r, float)

    def testTrolleyRoutes(self):
        routes = septapy.utils.trolleyRoutes()
        self.assertTrue('10' in routes)
        self.assertTrue('13' in routes)
        self.assertTrue('34' in routes)
        self.assertTrue('36' in routes)

if __name__ == '__main__':
    unittest.main()
