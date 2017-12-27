import os, errno

class Fstools:
    def mkdir(self,directory):
        """ """
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    def find_files(self, search_root, file_extension):
        """ """
        local_files_found = []
        for root, dirs, files in os.walk(search_root):
            for file in files:
                if file.endswith(file_extension):
                    found_file = os.path.join(root, file)
                    local_files_found.append(found_file)
        return local_files_found


