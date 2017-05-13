# Python Virtual Env Starter
Use this handy utility to make setting up your python projects "mad easy" for other developers.

Tons of thanks to @kennethreitz and @dasJ for making [autoenv](https://github.com/kennethreitz/autoenv) :)

### What does it do??
This script will create a few essential files in your repository:

##### .env
This file is used by autoenv to automatically switch to your python virtualenv and run any generic shell commands
(such as modifying your $PATH or $BIN, adding aliases, etc.) whenever you `cd` into your project directory.

##### setup.sh
This file allows developers who clone your repository to easily install OS-level dependencies


##### .gitignore
This will add or update your gitignore to inclue the virtual env.  You don't wanna source control that!


 - Install python3 and pip using either `brew` or `apt-get` (we figure out which)
 - Install [autoenv](https://github.com/kennethreitz/autoenv)
 - Add the autoenv activation script to your `~/.bashrc` (or whatever startup script you specify)
 - Create a .env file if one doesn't already exist (If you don't know what this is, look at [autoenv](https://github.com/kennethreitz/autoenv))
 - Add your virtual environment to your `.gitignore` file

### How do I do it??
It's easy peasy!  Just run
```
sudo pip install python-env
python-env setup
./setup.sh
```
You should now see two new files, `.env` and `setup.sh`

then commit your changes to your own repo :)