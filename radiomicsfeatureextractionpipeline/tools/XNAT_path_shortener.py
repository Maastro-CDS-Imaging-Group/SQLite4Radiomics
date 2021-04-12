### XNAT path shortener

import argparse
import os, shutil
from pathlib import Path
import logging
from tqdm import tqdm
from glob import glob

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("XNAT Downloader")

# parse the data
parser = argparse.ArgumentParser()
parser.add_argument("--old_xnat_path", help="Provide the directory path where the downloaded XNAT files are located, default is the current directory", default=".")
parser.add_argument("--new_xnat_path", help="Provide the directory path where you would like to store shortened XNAT files, default is the current directory", default=".")
parser.add_argument("--file_format", help="Provide the file format you would like to shorthen path to (start with '.'), default = .dcm", default=".dcm")
args = parser.parse_args()

# read args into the variables
root = args.old_xnat_path
root_new = args.new_xnat_path
file_format = args.file_format

# create the directory where shortened-path-files will be located
if not os.path.exists(root_new):
    os.makedirs(root_new)
    logger.info(f"The new directory was created: {root_new}")

# for every folder in the old root directory
for directory in tqdm(glob(root + "/*/")):
    
    # fix the slashes
    directory = directory.replace("\\", "/")
    
    # new directory name
    directory_new = root_new + directory.split("/")[-2]
    
    # create the patient directory if not existent
    if not os.path.exists(directory_new):
        os.makedirs(directory_new)
        #logger.info(f"The new directory was created: {directory_new}")
    
    # move every dicom file to shorten the name
    for item in glob(directory + "/**/*" + file_format, recursive=True):
        shutil.copy(item, directory_new + "/" + item.split("\\")[-1])
    #logger.info(f"Succesfully shortened all the {file_format} files from {directory.split('/')[-2]}")    

logger.info(f"Successfully shortened all the files in {len(glob(root + '/*/'))}")