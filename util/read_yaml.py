import yaml
from util.config import cm

class ReadYaml():

    def __init__(self):
        with open(cm.sekorm_dir, 'r', encoding='UTF-8') as file:
            self.yaml = yaml.safe_load(file)

    def __getitem__(self, item):
        return self.yaml[item]

if __name__ == '__main__':
    sekorm = ReadYaml()
    print('\n', sekorm['搜索框'])