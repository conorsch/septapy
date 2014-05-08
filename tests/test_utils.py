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
        # Lazy test, the getKML() call should raise exceptions on failure
        results = septapy.utils.getKML(mockdata.KMLURL)

    def testExtractCoordinatesFromKML(self):
        results = septapy.utils.getKML(mockdata.KMLURL)
        coords = septapy.utils.extractCoordinatesFromKML(results)
        print "COORDS IS TYPE: %s" % str(type(coords))
        self.assertIsInstance(coords, list)
        for c in coords:
            self.assertIsInstance(c, float)

    def testTrolleyRoutes(self):
        routes = septapy.utils.trolleyRoutes()
        self.assertTrue('10' in routes)
        self.assertTrue('11' in routes)
        self.assertTrue('13' in routes)
        self.assertTrue('15' in routes)
        self.assertTrue('34' in routes)
        self.assertTrue('36' in routes)

if __name__ == '__main__':
    unittest.main()
