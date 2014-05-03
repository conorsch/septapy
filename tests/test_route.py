import sys
import os
import unittest
sys.path.insert(0, os.path.abspath( os.path.join(os.path.dirname(__file__), '../septapy/') ))
import septapy
from septapy.route import Route
import mockdata

class TestRoute(unittest.TestCase):

    def setUp(self):
        # Print out name of method
        sys.stdout.flush()
        sys.stdout.write("\nRunning test '%s'..." % self._testMethodName)
        sys.stdout.flush()
        self.r = Route(mockdata.route)

    def testRouteCreation(self):
        r = Route(mockdata.route)
        self.assertEqual(r.identifier, str(mockdata.route))

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
        nearestStop = self.r.nearestStop(mockdata.cityHallLat, mockdata.cityHallLng)
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
        heading = self.r.guessHeading(mockdata.cityHallLat, mockdata.cityHallLng)
        self.assertEqual(heading, 'WestBound')
        self.assertNotEqual(heading, 'EastBound')

    def testGuessHeading34FromWestPhilly(self):
        heading = self.r.guessHeading(mockdata.westPhillyLat, mockdata.westPhillyLng)
        self.assertEqual(heading, 'EastBound')
        self.assertNotEqual(heading, 'WestBound')

    def testRouteLine(self):
        routeLine = self.r.routeLine()
        for p in routeLine:
            self.assertTrue(isinstance(p, float))

    def ztestGuessHeadingBSL(self):
        # No real-time location for BSL, so this test fails. 
        # Leaving here to add a custom exception for JSONDecodeError in requests.get()
        pass
        r = Route('BSL')
        heading = r.guessHeading(self.mockLat, self.mockLng)

    def testGuessRoute34(self):
        probableRoute = septapy.route.guessRoute(mockdata.westPhillyLat, mockdata.westPhillyLng)
        self.assertEqual(probableRoute, '34')

    def testGuessRoute10(self):
        probableRoute = septapy.route.guessRoute(mockdata.westPhillyLat2, mockdata.westPhillyLng2)
        self.assertEqual(probableRoute, '10')

if __name__ == '__main__':
    unittest.main()
