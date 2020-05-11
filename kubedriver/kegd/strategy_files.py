import os
from .exceptions import MissingKegDeploymentStrategyFileError

base_strategy_file = 'kegd.yaml'

class KegDeploymentStrategyFiles:

    OBJECTS_DIR = 'objects'
    STRATEGY_FILE = base_strategy_file
    STRATEGY_FILE_OPTIONS = [base_strategy_file, 'keg.yaml', 'kegd.yml', 'keg.yml']

    def __init__(self, root_path):
        self.root_path = root_path

    def get_strategy_file(self):
        for strategy_file_opt in KegDeploymentStrategyFiles.STRATEGY_FILE_OPTIONS:
            path = os.path.join(self.root_path, strategy_file_opt)
            if os.path.exists(path) and os.path.isfile(path):
                return path
        raise MissingKegDeploymentStrategyFileError(f'Deployment strategy file not found by any of the possible paths: {KegDeploymentStrategyFiles.STRATEGY_FILE_OPTIONS} (at: {self.root_path}')


    def get_object_file(self, object_file_name):
        sub_path = os.path.join(KegDeploymentStrategyFiles.OBJECTS_DIR, object_file_name)
        path = os.path.join(self.root_path, sub_path)
        if not os.path.exists(path):
            raise MissingKegDeploymentStrategyFileError(f'Deployment strategy files missing object file {object_file_name} (path: {sub_path})')
        if not os.path.isfile(path):
            raise MissingKegDeploymentStrategyFileError(f'Deployment strategy files missing object file {object_file_name}, the path exists but it is not a valid file (path: {sub_path})')
        return path