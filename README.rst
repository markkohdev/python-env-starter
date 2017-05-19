Python Env Starter
===============================
Getting your python repository setup for other developers to work on can be tedious and time consuming.  Use this small but handy utility to make setting up your python projects "mad easy" for other developers.

Tons of thanks to @kennethreitz and @dasJ for making [autoenv](https://github.com/kennethreitz/autoenv) :)
Also thanks to @bkuberek for showing me how to write CLIs for applications!  👍

Feel free to leave or send any feedback, always looking for ways to improve dis


What does it do??
---------------------------
This script will create a few essential files in your repository:

**.env**

This file is used by autoenv to automatically switch to your python virtualenv and run any generic shell commands
(such as modifying your $PATH or $BIN, adding aliases, etc.) whenever you `cd` into your project directory.
Feel free to set your own common environment variables, aliases, functions, etc. in here!

**setup.sh**

This file allows developers who clone your repository to easily install OS-level dependencies.
Add your own ``apt-get`` and ``brew`` dependencies to this.

**.gitignore**

This will add or update your ``.gitignore`` to include the virtual env and compiled python files.  You don't wanna source
control those!

How do I do it??
----------------------
It's easy peasy!  Just run

**Installation**

.. code-block:: bash

    sudo pip install python-env-starter


**Running it**

.. code-block:: bash

    python-env setup
    ./setup.sh
    source ~/.bashrc


You should now see the new files, ``.env``, ``setup.sh``, and ``.gitignore``

then just commit the new files to your own repo :)