# pyenvironments
The folders in this repository hold the files for recreating python virtual environments.
As python environments get very large, the number of dependencies and version conflicts among
packages can grow unmanageably.  These environments provide a baseline and sample code for new projects.

Each folder provides the requirements.txt and environment.yml file for an environment of the folders name.

    capture.bat is a Windows batch file for creating the requirements.txt and environment.yml from a current environment.
    generate.bat is a complementary batch file that creates an environment from those files.

Each folder may have its own README.md file and potentially different LICENSE text.

While the conda package manager is used generally, environments may include 
* PyPi only packages that can only be installed using pip
* supporting software like C++ compilers or non-python executables (eg GDAL for geopandas) 