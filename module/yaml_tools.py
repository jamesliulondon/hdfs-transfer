from yaml import load, dump, YAMLError
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
import ast


class Yamltools:
    """
    data = load(stream, Loader=Loader)
    output = dump(data, Dumper=Dumper)
    """

    def read_config(self,path):
        """ """
        with open(path) as stream: 
            try:
                data = load(stream, Loader=Loader)
            except YAMLError as err:
                print(err)
        return data

    def write_config(self, path, data):
        """ the data is actually a string """
        

        with open(path, 'w') as outfile:
            dump(data, outfile, default_flow_style=False)

