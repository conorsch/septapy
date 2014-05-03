import sys
import os
import unittest
sys.path.insert(0, os.path.abspath( os.path.join(os.path.dirname(__file__), '../septapy/') ))
import septapy

class TestStop(unittest.TestCase):

    def setUp(self):
        # Print out name of method
        print "\nRunning test '%s'..." % self._testMethodName
        self.mockRoute = str(34)
        # Hard-code lat & lng of eastern entrance to City Hall in Philadelphia
        self.mockLat, self.mockLng = 39.95232, -75.16283

    def testGetStopsByRoute(self):
        stops = septapy.stop.getStopsByRoute(self.mockRoute)
        for s in stops:
            self.assertIsInstance(s, septapy.stop.Stop)

    def testGetNearestStops(self):
        nearestStops = septapy.stop.getNearestStops(self.mockLat, self.mockLng, route=self.mockRoute)
        # Ensure multiple return values
        self.assertGreater(len(nearestStops), 1)
        for s in nearestStops:
            self.assertIsInstance(s, septapy.stop.Stop)


if __name__ == '__main__':
    unittest.main()

