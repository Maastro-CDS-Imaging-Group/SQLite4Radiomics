# SQLite4Radiomics

SQLite4Radiomics is an integration project of the popular PACS software *Conquest DICOM* with radiomics extraction package *pyradiomics* 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for usage and or development purposes. Make sure to check the [Software User Manual](https://github.com/Maastro-CDS-Imaging-Group/SQLite4Radiomics/blob/master/radiomicsfeatureextractionpipeline/Software%20User%20Manual.pdf) included in the project

Prior to using SQLite4Radiomics, we recommend to learn more about [*pyradiomics*](https://pyradiomics.readthedocs.io/en/latest/) and [*The Image Biomarker Standardization Initiative*](https://pubs.rsna.org/doi/full/10.1148/radiol.2020191145). In order to understand how pyradiomics feature extraction is customized, please refer to [*pyradiomics customization*](https://pyradiomics.readthedocs.io/en/latest/customization.html). Once you have made yourself familiar with these sources, you are better equipped to run radiomic analyses and customize pyradiomics extraction settings by the Parameter file modifications according to your needs.



## Built With

* [Angular](https://angular.io/docs) - The frontend framework used, typescript base

* [DJango](https://docs.djangoproject.com/en/3.0/) - The backend framework used, python based

* [Electron](https://www.electronjs.org/docs) - Framework used for the desktop client, javascript based

* [Conquest DICOM](https://ingenium.home.xs4all.nl/dicom.html) - Database and DICOM

## Contributing

We will not be keeping active management of the master branch and therefore will not be handling pull requests, as the norm. You can, however, fork and work on your own version of the tool with any improvements or variations you see fit.

## Authors and citation

* **Ivan Zhovannik** - *Initial idea, pipeline development, testing, and benchmarking* - Radboudumc Radiation Oncology department & [Maastro Clinic CDS Imaging group](https://github.com/Maastro-CDS-Imaging-Group)
* **Suraj Pai** - *Pipeline development, testing, and benchmarking* - Maastricht University & [Maastro Clinic CDS Imaging group](https://github.com/Maastro-CDS-Imaging-Group)
* **Talia Santos** - *GUI and production development* - Radboudumc Radiation Oncology department & Fontys University of Applied Sciences
* **Lars L.G. van Driel** - *Pipeline development* - Radboudumc Radiation Oncology department & Fontys University of Applied Sciences
* **Andre Dekker**, **Rianne Fijten**, **Alberto Traverso** - *Clinical support and medical imaging* - Maastro Clinic Clinical Data Science
* **Johan Bussink** - *Clinical support* - Radboudumc Radiation Oncology department
* **René Monshouwer** - *Principle Investigator* - Radboudumc Radiation Oncology department

The technical note about SQLite4radiomics is currently under review, we will update the citation as soon as the article published.

## License

This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details

Copyright (c) 2020 University of Manchester. Developed by Marcel van Herk, Lambert Zijp and Jan Meinders; the Netherlands Cancer Institute; Radiotherapy Department; maintained by Marcel van Herk, University of Manchester.

Copyright (c) 1995 Regents of the University of California. All rights reserved. Developed by: Mark Oskin, mhoskin@ucdavis.edu; University of California, Davis Medical Center; Department of Radiology with a Solaris port done and maintained by: Terry Rosenbaum; Michigan State University; Department of Radiology.

## Acknowledgments

The contributors would like to thank,

* The IBSI, 3D slicer and pyradiomics communities for providing valuable feedback on radiomics side of the project;
* Marcel van Herk for keeping the support of Conquest DICOM;
* plastimatch for making DICOM RT -> NRRD translation reproducible.

