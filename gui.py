"""
TODO: Name the App
"""



from flask import Flask, url_for
#from flask_restful import Resource, Api
from module.uri_tools import Sftp

#import subprocess


APP = Flask(__name__)


@APP.route('/gfi')
def gfi():
        """
        GFI
        """
        #fhost = 'data.gfigroup.com'
        #fpass = '0r63rR3c4p5'
        #fuser = 'orderrecapuser'
        sftp_object = Sftp()
        #print (fhost)
        sftp_session = sftp_object.connect('data.gfigroup.com', 'orderrecapuser', '0r63rR3c4p5')
        return "Hi"






if __name__ == '__main__':
    APP.run(debug=True)
