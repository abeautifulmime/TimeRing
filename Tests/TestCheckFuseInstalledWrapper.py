import xlrd
from Tests.TimeRingTestCase import TimeRingTestCase
from .check_fuse_installed_wrapper import checkFuse

class testCheckFuseInstalledWrapper(TimeRingTestCase):
    xls = None

    def setUpClass(cls):
        # get test data specific to test case.
        xls = super().open_test_data(cls.__class__.__name__)

    def test_check_path_length(self):
        #load data
        result = checkFuse._check_path_length([""])
        assert(result)

    def test_check_path_composition(self):
        raise NotImplementedError

    def test_check_dir_format(self):
        raise NotImplementedError

    def test_get_list_of_known_library_locations(self):
        raise NotImplementedError

    def test_format_bash_parameter_string(self):
        raise NotImplementedError

    def test_compile_bash_parameters():
        raise NotImplementedError

    def test_check_fuse_installed():
        raise NotImplementedError