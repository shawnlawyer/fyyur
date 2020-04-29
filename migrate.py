from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import Config
import importlib
import os

from app import app, db
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

MODELS_DIRECTORY = "models"
EXCLUDE_FILES = ["__init__.py"]

def import_models():
    for dir_path, dir_names, file_names in os.walk(MODELS_DIRECTORY):
        for file_name in file_names:
            if file_name.endswith("py") and not file_name in EXCLUDE_FILES:
                file_path_wo_ext, _ = os.path.splitext((os.path.join(dir_path, file_name)))
                module_name = file_path_wo_ext.replace(os.sep, ".")
                importlib.import_module(module_name)


if __name__ == '__main__':
    import_models()
    manager.run()
