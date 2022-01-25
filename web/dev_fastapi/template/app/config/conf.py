# %%
import yaml
from easydict import EasyDict
import os


class Config:
    def __init__(self, yaml_path='./app/config/conf.yaml'):
        with open(yaml_path, 'r') as f:
            j = yaml.load(f, Loader=yaml.FullLoader)
        self.conf = EasyDict(j)
        self.parse_env_var(self.conf, os.environ)
    
    def parse_env_var(self, item: dict, env: dict) -> dict:
        for k, v in item.items():
            if isinstance(v, str) and v.startswith('${') and v.endswith('}'):
                item[k] = env.get(v[2: -1])
            elif isinstance(v, dict):
                self.parse_env_var(v, env)


conf = Config().conf
