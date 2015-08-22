import unittest
from Tests.TimeRingTestCase import TimeRingTestCase


class TestTimeRingTestCase(unittest.TestCase):

    def testLoadTestConfig(self):
        result = TimeRingTestCase.testTestConfigFileExists()
        assert(result)

    def testDatabaseExists(self):
        result = TimeRingTestCase.testDatabaseExists()
        assert(result)

    def testTestConfigFileExists(self):
        result = TimeRingTestCase.testConfigFileExists()
        self.assertIsNotNone(result)