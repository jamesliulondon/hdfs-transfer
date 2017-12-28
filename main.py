#!/usr/bin/env python

hdfs_root = '/user/root'
local_root = '.'
ftp_root = '/upload/20171226'
ftp_host = '172.20.128.5'
ftp_user = 'jim'
ftp_pass = 'jim'

from module.hdfs import *
from module.date_tools import *
from module.yaml_tools import *
from module.business_logic import *
from module.fs_tools import *
from module.uri_tools import *
import ast

def main():
    """ 
    Main: Download files
        Post to FTP
    """
    ### Intitialise Objects
    # SFTP
    sftp_object = Sftp()


    ### Read LEI from FTP server
    
    sftp_session = sftp_object.connect(ftp_host, ftp_user, ftp_pass)
    active_leis = sftp_object.list(sftp_session,ftp_root)
    active_leis = ast.literal_eval(active_leis)

    authorised_lei_data={'authorised_lei': active_leis}
    print "MARKER"
    print active_leis
    print authorised_lei_data

    config_tool = Yamltools()
    config = config_tool.write_config('report.yml', authorised_lei_data)

    ### Read Config File
    config_reader = Yamltools()
    config = config_reader.read_config('report.yml')
    print "READ" + str(config['authorised_lei'])
    #for lei in config['authorised_lei']:
    #    print lei

    ### Get Date of files to search.
    t = Rtime()
    y = t.today(-1)
    short_date = t.reverse_short(y)
    search_path = hdfs_root + '/' + short_date

    ### Connect to HDFS to download list files. 'session' is the object
    conn = Connect()
    session = conn.connect()
    objects_found = conn.list(session, search_path)

    ### Select files to download
    logic = Filterlogic()
    selected_folders = logic.authorised_lei_files(objects_found, config['authorised_lei'])
    print selected_folders

    ### Create Destination directories
    fs = Fstools()
    for directory in config['authorised_lei']:
        fs.mkdir(local_root + '/' + t.reverse_short(y) + '/' + directory)

    ### Download files
    for folder in selected_folders:
        if conn.isdirectory(session, folder) is True:
            print 'Downloading'
            source = folder + '/' + logic.get_remote_filename()
            directory = folder.split('/')[-1]
            destination = local_root + '/' + short_date + '/' + directory + '/' + logic.get_local_filename(source)
            print  source + '   '  +  destination
            conn.download(session, source, destination)

    ### Upload files
    upload_list =  fs.find_files(local_root + '/' + short_date, '.txt')

    print upload_list
    for upload_file in upload_list:
        ftp_folder = logic.get_ftp_directory(upload_file)
        print ftp_folder
        sftp_object.upload(sftp_session, '/upload', upload_file, ftp_folder)
        
        




if __name__ == '__main__':
    main()