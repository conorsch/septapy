import sys
import os
import unittest
sys.path.insert(0, os.path.abspath( os.path.join(os.path.dirname(__file__), '../septapy/') ))
import septapy
from septapy.route import Route

class TestRoute(unittest.TestCase):

    def setUp(self):
        # Print out name of method
        sys.stdout.flush()
        sys.stdout.write("\nRunning test '%s'..." % self._testMethodName)
        sys.stdout.flush()
        self.mockRoute = 34
        # Hard-code lat & lng of eastern entrance to City Hall in Philadelphia
        self.mockLat, self.mockLng = 39.95232, -75.16283
        self.r = Route(self.mockRoute)

    def testRouteCreation(self):
        r = Route(self.mockRoute)
        self.assertEqual(r.identifier, str(self.mockRoute))

    def testVehicleLookup(self):
        vehicles = self.r.vehicles()
        for v in vehicles:
            self.assertEqual(v.route, self.r.identifier)

    def testStopLookup(self):
        stops = self.r.stops()
        for s in stops:
            self.assertEqual(s.route, self.r.identifier)

    def testTripLookup(self):
        trips = self.r.trips()
        for t in trips:
            self.assertEqual(t.route, self.r.identifier)

    def testNearestStop(self):
        # Hard-code lat & lng of eastern entrance to City Hall in Philadelphia
        nearestStop = self.r.nearestStop(self.mockLat, self.mockLng)
        self.assertEqual(nearestStop.name, '13th St Trolley Station')
        self.assertEqual(nearestStop.stopID, 283)

    def testDirections34(self):
        directions = self.r.directions()
        self.assertEqual(directions, ('EastBound', 'WestBound'))

    def ztestDirectionsBSL(self):
        # No real-time location for BSL, so this test fails. 
        # Leaving here to add a custom exception for JSONDecodeError in requests.get()
        pass
        r = Route('BSL')
        directions = r.directions()
        self.assertEqual(directions, ('NorthBound', 'SouthBound'))

    def testGuessHeading34FromCityHall(self):
        heading = self.r.guessHeading(self.mockLat, self.mockLng)
        self.assertEqual(heading, 'WestBound')
        self.assertNotEqual(heading, 'EastBound')

    def testGuessHeading34FromWestPhilly(self):
        # Hard-code lat & long for 60th & Cobbs Creek Parkway (West Philly)
        lat, lng = 39.9463, -75.2441
        heading = self.r.guessHeading(lat, lng)
        self.assertEqual(heading, 'EastBound')
        self.assertNotEqual(heading, 'WestBound')

    def testRouteLine(self):
        routeLine = self.r.routeLine()
        self.assertTrue(len(filter(lambda x: isinstance(x, float), routeLine)) == len(routeLine))

    def ztestGuessHeadingBSL(self):
        # No real-time location for BSL, so this test fails. 
        # Leaving here to add a custom exception for JSONDecodeError in requests.get()
        pass
        r = Route('BSL')
        heading = r.guessHeading(self.mockLat, self.mockLng)

    def ztestGuessRoute(self):
        # Hard-code lat & long for 60th & Cobbs Creek Parkway (West Philly)
        lat, lng = 39.9463, -75.2441
        probableRoute = septapy.route.guessRoute(lat, lng)
        self.assertEqual(probableRoute, '34')

if __name__ == '__main__':
    unittest.main()
