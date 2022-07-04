:: shell
::for dir in ./*/     :: list directories in the form "/tmp/dirname/"
::do
::    echo "$dir}"    :: print everything after the final "/"
::done
  ::  pip freeze > requirements.txt
  ::  conda env export > environment_droplet.yml  cd .
:: DOS

for /d %%d in (geotools machinelearning naturallanguage) do (
  cd %%d
  pip freeze > requirements.txt
  conda env export > environment.yml
  cd ..
  )

