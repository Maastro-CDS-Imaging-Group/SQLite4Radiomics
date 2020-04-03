"""
module:

Radiomic Feature Extraction Pipeline
====================================


About the tool
--------------

This module contains the source code of the radiomic feature extraction pipeline tool which is created by radboudumc, a
university medical center in The Netherlands.

The tool can be used for calculating radiomic features for tumors of a patient.

Packages
--------

To calculate the features the application makes use of 6 major packages::

    1. bootstrapper:
        This module will instantiate every thing that is needed for the calculation. It will boot up  the 5 other modules
        depending on the settings that it received through the initialisation file and the call that the user made.
    2. configuration_service:
        This module will interact with the initialisation file of the application. It will load and save properties that
        tell the tool how to run.
    3. gui:
        This module will manage the graphical user interface of the tool. This way the user will be able to interact with
        with the tool on a more user friendly way. The gui will be mostly used for configuring the initialisation file of
        the tool.
    4. cli:
        This module is for the more technical users of the tool. This command line interface module will let users who
        prefer to work with a command line use our radiomic feature extraction pipeline.
    5. logic:
        This module is the brain from the application. It keeps track of all the entities of the application and knows how
        Dicom files need to be loaded, how region of interest need to be selected and how features need to be extracted. It
        will receive a request from either the gui or the cli module and will handle the request correctly
    6. dal:
        This module is completely dedicated to storing results into the database and loading images, patients, scans, etc.
        The dal can be used for many types of databases and you can switch between them via the initialisation file.



**PLEASE DO NOT REMOVE!**

This file makes a module of the *src* directory.
This allows for the python interpreter to access the other python modules in this directory.
Without this file the python interpreter will not be able to find the modules in the directory!
"""