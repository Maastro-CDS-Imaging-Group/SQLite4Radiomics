import xnat
import argparse
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("XNAT Downloader")

parser = argparse.ArgumentParser()
parser.add_argument("--download_path", help="Provide path where the files are downloaded", default=".", type=Path)
parser.add_argument("--project_id", help="Provide ID for the XNAT project to download images", default="stwstrategyln1")
parser.add_argument("--username", help="Provide your username to gain access to private projects.", default=None)
parser.add_argument("--password", help="Provide your password for your user.", default=None)
args = parser.parse_args()

with xnat.connect('https://xnat.bmia.nl', user=args.username, password=args.password) as session:
    
    args.download_path.mkdir(parents=True, exist_ok=True)

    project = session.projects[args.project_id]
    logger.info(f'Total number of subjects {len(project.subjects)}')

    for i, subject in enumerate(project.subjects.values()):
        
        subject_path = args.download_path / subject.label

        if subject_path.exists():
            logger.info(f'Skipping {i+1}/{len(project.subjects)}: {subject.label} - {len(subject.experiments)} experiment(s)')
            continue
        
        logger.info(f'{i+1}/{len(project.subjects)}: {subject.label} downloading {len(subject.experiments)} experiment(s)')

        subject.download_dir(args.download_path)