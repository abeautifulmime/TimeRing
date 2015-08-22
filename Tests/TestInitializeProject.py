import unittest
from Tests.InitializeProject import InitializeProject

class  TestInitializeProjectTestCase(unittest.TestCase):

    def testTestConfigFileExists(self):
        result = InitializeProject.testConfigFileExists()
        assert(result)

    def testDoesDatabaseExist(self):
            result = InitializeProject.databaseExists()
            assert(result)
