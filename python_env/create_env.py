#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from builtins import input
import logging
import os
from jinja2 import Environment, PackageLoader

# Setup template and target files
PWD = os.environ.get('PWD', '.')

ENV_TEMPLATE = 'env.template'
ENV_TARGET = os.path.join(PWD, '.env')

SETUP_TEMPLATE = 'setup.template'
SETUP_TARGET = os.path.join(PWD, 'setup.sh')

GITIGNORE_TEMPLATE = 'gitignore.template'
GITIGNORE_TARGET = os.path.join(PWD, '.gitignore')


def main(args, logger=None):
    logger = logger or logging.getLogger()

    logger.info("Starting virtual env setup")

    venv_dir = args.dir
    python_ver = args.python

    # If we're interactive, prompt the users to update the values for things!
    if not args.non_interactive:
        venv_dir = input('Virtual environment name [{}]: '.format(venv_dir)) or venv_dir

        python_ver = input('Python interpreter [{}]: '.format(python_ver)) or python_ver

    # Sanitize our python version...this won't work if we don't
    if 'python2' not in python_ver and 'python3' not in python_ver and python_ver != 'python':
        logger.error('Invalid python interpreter.  Please use either python2 or python3.')
        sys.exit(1)

    # Initialize our jinja templates dir
    env = Environment(
        loader=PackageLoader('python_env', 'templates'),
    )

    template_args = {
        'venv_name': venv_dir,
        'python': python_ver,
        'pip': 'pip3' if 'python3' in python_ver else 'pip'
    }

    ###########################################################################
    # .env
    ###########################################################################
    template = env.get_template(ENV_TEMPLATE)
    with open(ENV_TARGET, 'w') as fh:
        fh.write(template.render(**template_args))

    # chmod 755 (in octal, because wtf python)
    os.chmod(ENV_TARGET, 493)

    ###########################################################################
    # setup.sh
    ###########################################################################
    template = env.get_template(SETUP_TEMPLATE)
    with open(SETUP_TARGET, 'w') as fh:
        fh.write(template.render(**template_args))

    # chmod 755 (493 in decimal = 755 in octal, because wtf python)
    os.chmod(SETUP_TARGET, 493)

    ###########################################################################
    # .gitignore
    # This very well may already exist, so we just wanna update it if it does
    ###########################################################################
    template = env.get_template(GITIGNORE_TEMPLATE)
    template_lines = template.render(**template_args).splitlines()
    with open(GITIGNORE_TARGET, 'a+') as fh:
        fh.seek(0)
        gitignore_lines = [line.strip() for line in fh.readlines()]
        for line in template_lines:
            if line not in gitignore_lines:
                logger.debug('Adding "{}" to .gitignore'.format(line))
                fh.writelines([line])
            else:
                logger.debug('"{}" already exists in .gitignore'.format(line))

    print("""
Python env setup complete!  Please run
  ./setup.sh
""")

    logger.info("Python env setup complete!")


# Main Runner
if __name__ == "__main__":
    main([])
