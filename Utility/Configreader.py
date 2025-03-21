from configparser import RawConfigParser

config = RawConfigParser()
config.read("C:/Users/KIIT/PycharmProjects/pythonProject6/Configuration/config.ini")


class Configurations:
    @staticmethod
    def get_url():
        url = config.get('DJ','url')
        return url