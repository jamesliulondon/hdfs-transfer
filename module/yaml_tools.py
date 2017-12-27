from yaml import load, dump, YAMLError
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


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
            except yaml.YAMLError as err:
                print(err)
        return data
