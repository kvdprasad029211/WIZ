import configparser
config = configparser.RawConfigParser()
config.read(".\\WIZ_TESTING\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getAppURL():
        url = config.get('Common Data','baseURL')
        return url
    @staticmethod
    def getuser():
        username = config.get('Common Data','username')
        return username
    @staticmethod
    def getpass():
        password = config.get('Common Data','password')
        return password