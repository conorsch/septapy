# This test structure was recommended in SO Answer
# http://stackoverflow.com/a/2992477. Very convenient for 
# bootstrapping a test env for new cloners of the repo.
import glob
import unittest
import os

def create_test_suite():
    """Returns a TestSuite object of everything in the tests/ dir"""

    testDir = 'tests'
    test_file_strings = glob.glob(os.path.join(testDir, 'test_*.py'))

    module_strings = [testDir + '.' + s[6:len(s)-3] for s in test_file_strings]
    suites = [unittest.defaultTestLoader.loadTestsFromName(name) \
              for name in module_strings]
    testSuite = unittest.TestSuite(suites)

    return testSuite
