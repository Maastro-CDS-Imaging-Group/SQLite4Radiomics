# SQLite4Radiomics

SQLite4Radiomics is an integration project of the popular PACS software *Conquest DICOM* with radiomics extraction package *pyradiomics* 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for usage and or development purposes. Make sure to check the Software User Manual included in the project.

### Prerequisites

What things you need to run the software and how to install them.

SQLite4Radiomics was originally written for Windows 10 platform. It should in principle, also work on windows 7/8/8.1. Other platforms are not fully supported.

#### Python and NodeJS are required to run this software tool.

The user should also have some experience with working with Radiomics.

Prior to using SQLite4Radiomics, we recommend to learn more about (*pyradiomics documentation*)[https://pyradiomics.readthedocs.io/en/latest/] and (*The Image Biomarker Standardization Initiative*)[https://pubs.rsna.org/doi/full/10.1148/radiol.2020191145]. In order to understand how pyradiomics feature extraction is customized, please refer to

```
https://pyradiomics.readthedocs.io/en/latest/customization.html
```

Once you have read this, you are better equipped to run radiomic analyses and customize pyradiomics extraction settings by the Parameter file modifications according to your needs.

#### Python

Go to https://www.python.org/downloads/release/python-365/ and download the appropriate installer for your system.

Follow the necessary steps to install python 3.6.5

Make sure that you choose the option during installation to add python to the Path.

#### NodeJs
Go to https://nodejs.org/en/ and download the appropriate installer for your system.
Follow the necessary steps to install NodeJs.

#### Clone the repository
Clone the git repository with

```
git clone https://github.com/Maastro-CDS-Imaging-Group/SQLite4Radiomics
```


#### Setting up

Run the Setup.bat file. This will make sure that:

1. the paths that Conquest uses, matches the current location on your machine

2. creates the necessary virtual environment and installs the necessary python packages

3. installs necessary node packages

You should see a command prompt window pop up and go through the installation of the necessary packages.

If when running this file, the command prompt window immediately closes after execution (no package installation could be seen), then check the Troubleshooting section below.

#### Data

Go to the conquest folder and run ConquestDICOMServer.exe

When Conquest is running, go to the data folder and open the incoming folder within. Drop your DICOM files here while Conquest is running. 

#### Operation

Run the Sqlite4Radiomics.bat file to start up the tool.

#### Troubleshooting
##### Python 2

If you have python 2.x installed, this could lead to some problems when setting up the tool. If you get any errors when running Setup.bat, please find your python installation, usually at (or something similar):
```
C:\Users\username\AppData\Local\Programs\Python\Python36
```
(note that username should be the name of the profile on your machine)


In this folder there is a Python.exe file. Make a copy of this file and rename it to Python3.exe

In the folder where the Sqlite4Radiomics is located, there is a scripts folder. Within, you can find a batch file named venv-setup.bat.

Open this file in edit mode and substitute the “py -3.6” with “python3”. Save and close the file. The Setup.bat file should now be able to run without any further complications.

##### Terminal Errors

If you modify the configuration file and something goes wrong, the terminal should show that an error has occurred. All that needs to be done is to restore your configuration file. This can be done either in the interface. 

If this doesn’t work, go to backend -> resources -> backups where you should find the default and previous versions of the files that can be modified. Copy the file you need into the resources folder, rename it to the correct name and delete the bad file.

If your problem is not related to the above-mentioned reasons, it is advised that you “re-install” the tool or contact an IT specialist.

##### CSV and Logs

If you want to find your outputted csv files yourself instead of downloading them, these can be found in backend -> out. 

Similarly, log files can be found in backend -> logs.

## Built With

* [Angular](https://angular.io/docs) - The frontend framework used, typescript base

* [DJango](https://docs.djangoproject.com/en/3.0/) - The backend framework used, python based

* [Electron](https://www.electronjs.org/docs) - Framework used for the desktop client, javascript based

* [Conquest DICOM](https://ingenium.home.xs4all.nl/dicom.html) - Database and DICOM

## Contributing

We will not be keeping active management of the master branch and therefore will not be handling pull requests, as the norm. You can, however, fork and work on your own version of the tool with any improvements or variations you see fit.

## Authors and citation

* **Ivan Zhovannik** - *Initial idea, backend development, testing, and benchmarking* - Radboudumc Radiation Oncology department & [Maastro Clinic CDS Imaging group](https://github.com/Maastro-CDS-Imaging-Group)
* **Suraj Pai** - *Backend development, testing, and benchmarking* - Maastricht University & [Maastro Clinic CDS Imaging group](https://github.com/Maastro-CDS-Imaging-Group)
* **Talia Santos** - *GUI and production development* - Radboudumc Radiation Oncology department & Fontys University of Applied Sciences
* **Lars L.G. van Driel** - *Initial development* - Radboudumc Radiation Oncology department & Fontys University of Applied Sciences
* **Andre Dekker**, **Rianne Fijten**, **Alberto Traverso** - *Clinical support and medical imaging* - Maastro Clinic Clinical Data Science
* **Johan Bussink** - *Clinical support* - Radboudumc Radiation Oncology department
* **René Monshouwer** - *Principle Investigator* - Radboudumc Radiation Oncology department

The technical note about SQLite4radiomics is currently under review, we will update the citation as soon as the article published.

## License

This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details

Copyright (c) 2020 University of Manchester. Developed by Marcel van Herk, Lambert Zijp and Jan Meinders; the Netherlands Cancer Institute; Radiotherapy Department; maintained by Marcel van Herk, University of Manchester.

Copyright (c) 1995 Regents of the University of California. All rights reserved. Developed by: Mark Oskin, mhoskin@ucdavis.edu; University of California, Davis Medical Center; Department of Radiology with a Solaris port done and maintained by: Terry Rosenbaum; Michigan State University; Department of Radiology.

## Acknowledgments

The contributors would like to thank 
* The IBSI, 3D slicer and pyradiomics communities for providing valuable feedback on radiomics side of the project;
* Marcel van Herk for keeping the support of Conquest DICOM;
* plastimatch for making DICOM RT -> NRRD translation reproducible.

