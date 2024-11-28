import os

class ConfigManger():

    @property
    def ini_dir(self):
        dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.ini')
        return dir

    @property
    def sekorm_dir(self):
        dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'element\sekorm.yml')
        return dir

cm = ConfigManger()

if __name__ == '__main__':
    print('\n', cm.sekorm_dir)