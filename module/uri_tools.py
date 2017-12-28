import pysftp

class Sftp:
    def connect(self, hostname, username, password):
        session = pysftp.Connection(hostname, username='jim', password='jim') 
        return session
    
    def upload(self, session, cwd='.', file='foo.txt', new_folder=''):
        tmp_dir_path = cwd
        if new_folder != '':
            new_folder_array = new_folder.split('/')
            for folder_element in new_folder_array:
                tmp_dir_path = tmp_dir_path + '/' + folder_element
                print tmp_dir_path
                if (session.isdir(tmp_dir_path) is False):
                    session.mkdir(tmp_dir_path)
            session.cd(tmp_dir_path)
        with session.cd(tmp_dir_path):
            print 'uploading ' + file
            session.put(file)

    def list(self, session,remotepath):
        found_folders = session.listdir(remotepath)
        print str(found_folders)
        return str(found_folders)





