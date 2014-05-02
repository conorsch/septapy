#!/usr/bin/env python
# This test harness structure was recommended in SO Answer
# http://stackoverflow.com/a/2992477. Very convenient for 
# bootstrapping a test env for new cloners of the repo.
# Also requires relative imports in the individual test files.
import unittest
import tests.all_tests
testSuite = tests.all_tests.create_test_suite()
text_runner = unittest.TextTestRunner().run(testSuite)
