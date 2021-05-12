# Troubleshooting
## Python 2

If you have python 2.x installed, this could lead to some problems when setting up the tool. If you get any errors when running Setup.bat, please find your python installation, usually at (or something similar):
```
C:\Users\username\AppData\Local\Programs\Python\Python36
```
(note that username should be the name of the profile on your machine)


In this folder there is a `Python.exe` file. Make a copy of this file and rename it to `Python3.exe`

In the folder where the Sqlite4Radiomics is located, there is a scripts folder. Within, you can find a batch file named `venv-setup.bat`.

Open this file in edit mode and substitute the `py -3.6` with `python3`. Save and close the file. The Setup.bat file should now be able to run without any further complications.

## Terminal Errors

If you modify the configuration file and something goes wrong, the terminal should show that an error has occurred. All that needs to be done is to restore your configuration file. This can be done either in the interface. 

If this doesn’t work, go to `backend\resources\backups` where you should find the default and previous versions of the files that can be modified. Copy the file you need into the resources folder, rename it to the correct name and delete the bad file.

If your problem is not related to the above-mentioned reasons, it is advised that you “re-install” the tool or contact an IT specialist.