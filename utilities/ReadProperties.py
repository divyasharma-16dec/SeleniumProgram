import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.join(os.path.dirname(__file__),"..","configurations","config.ini"))

class ReadProperties:
    @staticmethod
    def get_URL():
        return config.get("common info","baseURL")

    @staticmethod
    def get_emaiid():
        return config.get("common info","login_email")


x
