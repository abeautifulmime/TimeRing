import  xml.etree.cElementTree as ET

class InitializeProject(object):
    _test_config_uri = "aplication_config.xml"
    _test_database_selector = "test_databae_uri"

    @classmethod
    def databaseExists(cls):
        pass

    @classmethod
    def testConfigFileExists(cls):
        root = ET.parse(cls._test_config_uri).getroot()
        return root is not None