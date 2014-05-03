import sys
import os
import unittest
sys.path.insert(0, os.path.abspath( os.path.join(os.path.dirname(__file__), '../septapy/') ))
import septapy

class TestUtils(unittest.TestCase):

    def setUp(self):
        # Print out name of method
        sys.stdout.flush()
        sys.stdout.write("\nRunning test '%s'..." % self._testMethodName)
        sys.stdout.flush()
        self.mockRoute = str(34)
        self.mockKMLURL = 'http://www3.septa.org/transitview/kml/%s.kml' % self.mockRoute
        # Hard-code lat & lng of eastern entrance to City Hall in Philadelphia
        self.mockLat, self.mockLng = 39.95232, -75.16283

    def testGetKML(self):
        results = septapy.utils.getKML(self.mockKMLURL)
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
