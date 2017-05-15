Python Env Starter
===============================
Getting your python repository setup for other developers to work on can be tedious and time consuming.  Use this handy
utility to make setting up your python projects "mad easy" for other developers.

Tons of thanks to @kennethreitz and @dasJ for making [autoenv](https://github.com/kennethreitz/autoenv) :)

What does it do??
---------------------------
This script will create a few essential files in your repository:

**.env**
This file is used by autoenv to automatically switch to your python virtualenv and run any generic shell commands
(such as modifying your $PATH or $BIN, adding aliases, etc.) whenever you `cd` into your project directory.

**setup.sh**
This file allows developers who clone your repository to easily install OS-level dependencies.

**.gitignore**
This will add or update your gitignore to include the virtual env and compiled python files.  You don't wanna source
control that!

How do I do it??
----------------------
It's easy peasy!  Just run

.. code:: bash

    sudo pip install python-env
    python-env setup
    ./setup.sh


You should now see the new files, ``.env``, ``setup.sh``, and ``.gitignore``

then commit the changes to your own repo :)