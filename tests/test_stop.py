import sys
import os
import unittest
sys.path.insert(0, os.path.abspath( os.path.join(os.path.dirname(__file__), '../septapy/') ))
import septapy

class TestStop(unittest.TestCase):

    def setUp(self):
        # Print out name of method
        print "\nRunning test '%s'..." % self._testMethodName
        self.mockRoute = 34

    def testGetStopsByRoute(self):
        r = septapy.route.Route(self.mockRoute)
        r.identifier == self.mockRoute

if __name__ == '__main__':
    unittest.main()

