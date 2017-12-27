
from hdfs3 import HDFileSystem

default_namenode_host = '172.17.0.3'
default_namenode_port = 9000
default_root = '/'
Err = ''


class Connect:

    def connect(self,namenode_host=default_namenode_host, namenode_port=default_namenode_port):
        """
        hdfs
        """
        hdfs = HDFileSystem(namenode_host, namenode_port)
        return hdfs

    def list(self, conn, path=default_root):
        """ """
        return conn.ls(path)

    def download(self, conn, source, destination):
        """ """
        try:
            conn.get(source, destination)
        except Err:
            return (Err)

    def isdirectory(self, conn, path='/'):
        """ """
        try:
            print ((conn.info(path)['kind'] == 'directory') > 0)
            ((conn.info(path)['kind'] == 'directory') == 0)
            return True
        except Err:
            return Err
