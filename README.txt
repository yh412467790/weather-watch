symbol_check

Simple python script that uses a REST API exposed by api.openweathermap.org
Have been running with python 3.7.
Usage:  "python3.7 weather_check.py"
Opens config.ini and retrieves current weather info for zip codes listed, one per line.

If docker is installed and running, ./build.sh creates a docker container with the script. After running 
the build script, run with "docker run weather_check" 
