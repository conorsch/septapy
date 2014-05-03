import sys
import os
import unittest
sys.path.insert(0, os.path.abspath( os.path.join(os.path.dirname(__file__), '../septapy/') ))
import septapy

class TestVehicle(unittest.TestCase):

    def setUp(self):
        # Print out name of method
        sys.stdout.flush()
        sys.stdout.write("\nRunning test '%s'..." % self._testMethodName)
        sys.stdout.flush()
        self.mockRoute = str(34)

    def testGetVehiclesByRoute(self):
        vehicles = septapy.vehicle.getVehiclesByRoute(self.mockRoute)
        for v in vehicles:
            self.assertEqual(v.route, self.mockRoute)

if __name__ == '__main__':
    unittest.main()

