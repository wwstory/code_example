# %%
import yaml
from easydict import EasyDict


class Config:
    def __init__(self, yaml_path='./app/config/conf.yaml'):
        with open(yaml_path, 'r') as f:
            j = yaml.load(f, Loader=yaml.FullLoader)
        self.conf = EasyDict(j)

conf = Config().conf
