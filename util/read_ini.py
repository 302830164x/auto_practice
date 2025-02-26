import configparser

from util.config import cm


class ReadINI():

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(cm.ini_dir)

    def _get(self, setion, value):
        return self.config[setion][value]

    @property
    def SekormUrl(self):
        return self._get('url', 'sekorm')

ini = ReadINI()

if __name__ == '__main__':
    print('\n', ini.SekormUrl)