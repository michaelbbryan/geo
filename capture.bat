::
:: For the requested python environment, this captures the env.yml and reqs.txt  pyenvironment files
::

@echo off

@echo off
if [%1]==[] goto usage
if [%2]!=[] goto usage

SETLOCAL

:: for /d %envname% in (base geotools machinelearning naturallanguage financialmarkets dataengineering) do (
  conda activate %envname%
  if errorlevel 0 (
    echo %envname%
    cd %envname%
    pip list --format=freeze > requirements.txt
    conda env export > environment.yml
    conda env export -n %envname% > environment.yml
    cd ..
    )
  )

ENDLOCAL
@echo done
goto :eof

:usage
@echo Usage: %0 ^<EnvironmentName^>


