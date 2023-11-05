import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO)

project_name="test"
list_of_files = [".gitgub/workflow/.gitkeep"
                 f"src/test/__init__.py",
                 f"src/{project_name}/__init__.py",
                 f"src/{project_name}/compoenets/__init__.py",
                 f"src/{project_name}/components/data_ingestion.py",
                 f"src/{project_name}/components/data_transformation.py",
                 f"src/{project_name}/components/model/model_train.py",
                 f"src/{project_name}/components/model/model_monetring.py",
                 f"src/{project_name}/pipelines/__init__.py",
                 f"src/{project_name}/pipelines/training_piplines.py",
                 f"src/{project_name}/pipelines/prediction_pipline.py",
                 f"src/{project_name}/exception.py",
                 f"src/{project_name}/loger.py",
                 f"src/{project_name}/utils.py",
                 "app.py",
                 "Dockerfile",
                 "requirements.txt",
                 "setup.py",
                 "mean.py"]
for filepath in list_of_files:
    filepath= Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):

        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:

        logging.info(f"{filepath}is aboidy exists")
