::
:: Creates a python environment from the pyenvironment files
::     and installs it into the ipython kernel for work in Jupyter
::

echo off
if [%1]==[] goto usage
if NOT [%2]==[] goto usage

echo setting local
::SETLOCAL

SET envname=%1
:: FOR /D %%d in (*) do (    )

echo off
echo starting
echo %envname%
::conda activate %envname% >nul 2>nul
::if errorlevel 1 (
echo Creating %envname% environment
cd %envname%
conda env create -n %envname% -f environment.yml 
::>nul
echo adding it to ipy kernel
ipython kernel install --user --name=%envname% 
::>nul
echo back to base
conda activate base 
::>nul
cd ..
::     ) else (echo Environment %envname% already exists)
echo ending local
::ENDLOCAL
echo done
goto :eof

:usage
echo Usage: %0 ^<EnvironmentName^>


