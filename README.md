# Python Virtual Env Starter
Use this handy script to make setting up your python projects "mad easy" for other developers.

Tons of thanks to @kennethreitz and @dasJ for making [autoenv](https://github.com/kennethreitz/autoenv) :)

### What does it do??
This script will
 - Install python3 and pip using either `brew` or `apt-get` (we figure out which)
 - Install [autoenv](https://github.com/kennethreitz/autoenv)
 - Add the autoenv activation script to your `~/.bashrc` (or whatever startup script you specify)
 - Create a .env file if one doesn't already exist (If you don't know what this is, look at [autoenv](https://github.com/kennethreitz/autoenv))
 - Add your virtual environment to your `.gitignore` file

### How do I do it??
It's easy peasy!  Just run
```
./setup.sh
cd .
```
then commit your changes to your own repo :)