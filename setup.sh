#!/bin/bash
#
# setup.sh
# Written by Mark Koh
# 2/24/2017
#
# This script will install apt-get and brew dependencies into a python virtual environment as well as install autoenv
# which will automatically activate your virtual environment when you `cd` into this directory.

# Set this to whatever you so choose, just make sure it's in the .gitignore
read -p "Virtual environment name [env]: " VIRTUAL_ENV_NAME
VIRTUAL_ENV_NAME=${VIRTUAL_ENV_NAME:-env}

# See if we have either brew or apt-get installed
BREW_CMD=$(which brew)
APT_CMD=$(which apt-get)

if [[ ! -z $BREW_CMD ]]; then
    # What to install with `brew`
    echo "Installing python3...";
    brew install python3

elif [[ ! -z $APT_CMD ]]; then
    # What to install with `apt-get`
    echo "Installing python3...";
    sudo apt-get install -y python3 python3-pip
else
    echo "Neither brew nor apt-get are installed.  Exiting..."
    exit 1;
fi

echo "Installing virtualenv and autoenv...";
pip3 install virtualenv autoenv

read -p "Bash startup file [~/.bashrc]: " BASHRC
BASHRC=${BASHRC:-~/.bashrc}
BASHRC_ABS=`eval echo ${BASHRC//>}`

# Check if their bash file has autoenv activated in it, if not, see if they want to add it
if ! grep -q "activate.sh" $BASHRC_ABS ; then
    read -r -p "Do you want to add autoenv to your $BASHRC (recommended)? [y/n] " response
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])+$ ]]
    then
        echo "Adding autoenv to $BASHRC...";
        echo "# Activate autoenv" >> $BASHRC_ABS
        echo "source `which activate.sh`" >> $BASHRC_ABS
        echo "cd ." >> $BASHRC_ABS
    fi
fi

# Create the actual virtualenv
if [ ! -d $VIRTUAL_ENV_NAME ]; then
    echo "Creating virtual env..."
    virtualenv -p python3 $VIRTUAL_ENV_NAME

    if ! grep -q "$VIRTUAL_ENV_NAME" .gitignore; then
        echo "Adding virtual environment to .gitignore";
        echo "$VIRTUAL_ENV_NAME/" >> .gitignore
    fi
fi

# Setup .env file if not exists
if [ ! -e .env ]; then
    echo "Creating autoenv .env file...";
    cat << EOF > .env
venv=$VIRTUAL_ENV_NAME
currentvenv=""

if [[ \$VIRTUAL_ENV != "" ]]
then
  # Strip out the path and just leave the env name
  currentvenv="\${VIRTUAL_ENV##*/}"
fi

if [[ "\$currentvenv" != "\$venv" ]]
then
  echo "Switching to environment: \$venv"
  source ./\$venv/bin/activate
fi
EOF
  chmod +x .env
fi

# Source the bash setup file so we activate the autoenv
source $BASHRC_ABS
