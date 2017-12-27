class Filterlogic:
    """ """

    def authorised_lei_files(self, files, lei_filter):
        """
        returns if filename is in lei list
        """
        print ('LEI Filter: ' + str(lei_filter))
        return filter(lambda file: str(file).split('/')[-1] in lei_filter, files)

    def get_remote_filename(self):
        return 'output.txt'

    def get_local_filename(self,source_path):
        folder = source_path.split('/')[-2] # Normally the LEI
        print 'new filename ' + folder + '.txt'
        return folder + '.txt'

    def get_ftp_directory(self, source_path):
        folder1 = source_path.split('/')[-3] # Normally the date
        folder2 = source_path.split('/')[-2] # Normally the LEI
        return folder1 + '/' + folder2
         