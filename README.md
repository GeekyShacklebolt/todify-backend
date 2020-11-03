Todify
==============================

__Version:__ 0.0.0

Backend for Todify Project.

Minimum requirements: **pip, python3.8, [PostgreSQL 12][install-postgres]**. 
(Setup is tested on Mac OSX only)

    brew install libmagic postgresql python3

[install-postgres]: http://www.gotealeaf.com/blog/how-to-install-postgresql-on-a-mac

## Setting up 

### Get the code

In your terminal, type or copy-paste the following:

    git clone git@github.com:GeekyShacklebolt/todify-backend.git

### Create a python virtual environment

You can use the tool of your choice to create python virtualenv. Todify is based on python==3.8.0.

    cd todify-backend
    pyenv install 3.8.0
    pyenv virtualenv 3.8.0 todify
    pyenv activate todify 

### Install requirements and build dependecies

    make install

### Start the Django server

    make run

The `Makefile` in the project also support the following useful commands:

- `make check` - Runs default Django and linting checks
- `make clean` - Remove all temporary files like pycache, etc
- `make help` - Display all the avaialable options in `Makefile`
