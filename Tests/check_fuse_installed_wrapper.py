import subprocess

class checkFuse():
    @classmethod
    def _check_path_length(cls,path_list):
        return lambda path_list: len(path_list)==1
    @classmethod
    def _check_path_composition(cls,path):
         #regex here.
        raise NotImplementedError
    @classmethod
    def _check_dir_format(cls,line):
        if cls._check_path_length(line) and cls._check_path_composition(line[0]):
            return line[0]
        raise FileExistsError("Improperly formatted internal File")
    @classmethod
    def _get_list_of_known_library_locations(cls):
        known_paths=open("file_paths")
        list_of_arguments = []
        [list_of_arguments.append(cls._check_dir_format(path)) for path in known_paths]
        return list_of_arguments
    @classmethod
    def _format_bash_parameter_string(cls,list_of_arguments):
        return_parameter_format = "{0} "
        bash_arguments_to_be_called = None
        [bash_arguments_to_be_called.append(return_parameter_format.format(x)) for x in list_of_arguments()]
    @classmethod
    def _compile_bash_parameters(cls):
        list_of_library_locations = cls._get_list_of_known_library_locations()
        list_of_library_locations = cls._format_bash_parameter_string(list_of_library_locations)
        return list_of_library_locations
    @classmethod
    def check_fuse_installed(cls):
            bash_arguments_to_be_called = cls._compile_bash_parameters()
            subprocess.call(args=bash_arguments_to_be_called,executable="fuse_installed.sh",shell=True)