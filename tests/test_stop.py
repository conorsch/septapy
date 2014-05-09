import sys
import os
import unittest
sys.path.insert(0, os.path.abspath( os.path.join(os.path.dirname(os.path.dirname(__file__)), 'septapy') ))
import septapy
import mockdata

class TestStop(unittest.TestCase):

    def setUp(self):
        # Print out name of method
        sys.stdout.flush()
        sys.stdout.write("\nRunning test '%s'..." % self._testMethodName)
        sys.stdout.flush()

    def testGetStopsByRoute(self):
        stops = septapy.stop.getStopsByRoute(mockdata.route)
        for s in stops:
            self.assertIsInstance(s, septapy.stop.Stop)

    def testGetNearestStops(self):
        nearestStops = septapy.stop.getNearestStops(mockdata.locationCityHallLat, mockdata.locationCityHallLng, route=mockdata.route)
        # Ensure multiple return values
        self.assertGreater(len(nearestStops), 1)
        for s in nearestStops:
            self.assertIsInstance(s, septapy.stop.Stop)


if __name__ == '__main__':
    unittest.main()

