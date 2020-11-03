.DEFAULT_GOAL := help
SHELL := bash
.ONESHELL:

PROJECT_NAME=todify
DB_NAME=$(PROJECT_NAME)

install: ## Install requirements and setup project dependencies
	     python -m pip install -r requirements.txt
	     createdb $(DB_NAME)
	     psql -d $(DB_NAME) -c "create extension citext;"
	     python manage.py migrate
.PHONY: install

check: ## Runs django and linting checks
	   python manage.py check
	   flake8 .
.PHONY: check

clean:  ## Remove all temporary files like pycache
	    find . -name \*.rdb -type f -ls -delete
	    find . -name \*.pyc -type f -ls -delete
	    find . -name __pycache__ -ls -delete
.PHONY: clean

help:  ## Display this help
	   # https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	   @grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'
.PHONY: help

