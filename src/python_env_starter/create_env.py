# -*- coding: utf-8 -*-
# Copyright © 2017 Spotify AB
import logging
import os
import shutil
from jinja2 import Environment, PackageLoader

ENV_TEMPLATE = 'templates/env.template'
ENV_FILE = '.env'

def main(args, logger=None):
    logger = logger or logging.getLogger()

    logger.info("Starting virtual env setup")

    venv_dir = args.dir

    overwrite_env = True

    # Use these to compile file targets
    pwd = os.environ.get('PWD', '.')
    file_dir = os.path.dirname(__file__)

    env_target = os.path.join(pwd, ENV_FILE)

    # If we're interactive, prompt the users to update the values for things!
    if not args.non_interactive:
        venv_dir = input('Virtual environment directory [{}]: '.format(venv_dir)) or venv_dir

    env = Environment(
        loader=PackageLoader('python_env_starter', 'templates'),
    )

    # Copy template/env.template to .env (overwrite if exists
    shutil.copy(os.path.join(file_dir, ENV_TEMPLATE), env_target)
    # Replace template values in .env
    # chmod file

    # Copy template/setup.template to setup.sh
    # shutil.copy('template/env.template', '.env')

    # Replace template values in setup.sh
    # chmod file

    # Add venv to gitignore
    # if


    logger.info("Virtual env setup complete!")


# Main Runner
if __name__ == "__main__":
    main()
