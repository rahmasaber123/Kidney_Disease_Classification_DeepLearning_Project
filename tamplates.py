import os
from os import path
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "tamplates/index.html",
    
]
for file in list_of_files:
    file_path = path.join(os.getcwd(), file)
    file_dir = path.dirname(file_path)
    try:
        if not path.exists(file_dir):
            os.makedirs(file_dir)
            logging.info(f"Created directory: {file_dir}")
        if not path.exists(file_path):
            with open(file_path, "w") as f:
                pass
            logging.info(f"Created file: {file_path}")
        else:
            logging.info(f"File already exists: {file_path}")
    except Exception as e:
        logging.error(f"Error creating file {file_path}: {e}")