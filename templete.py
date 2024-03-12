import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format= '[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/logging/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath) #to take care of the path formats for the native OS
    filedir,filename = os.path.split(filepath) # to get the dir path and file name in separate variables

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating the dir {filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) != 0): # Check if the file doesn't exist or if it exists, it's not empty
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating the empty file {filename}")
    else:
        logging.info(f"The file {filename} already exists")