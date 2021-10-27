import os 
class Config(object):
    SECRET_KEY  = os.environ.get('SECRET_KEY') or "b'k(\xb4;\xce\x1av\xd9z\x9f\xfd\xbd25\xa2\xc7'"
    MONGODB_SETTINGS = {'db':'UTA_Enrollment'}