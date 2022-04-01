##############################################
# Make File Spec
# https://www.gnu.org/software/make/
# https://www.gnu.org/software/make/manual/html_node/Special-Targets.html
##############################################


# AUTO DETECT CORRECT LOCAL PYTHON / PIP
# AB-895: workaround windows has python symlinks to non-functional python3
# so "which python3" not enough
ifeq ($(shell python3 --version 2> /dev/null),)
	PYTHON = python
else
	PYTHON = python3
endif
ifeq ($(shell which pip3 2> /dev/null),)
	PIP = pip
else
	PIP = pip3
endif


.PHONY: install lint test

##############################################
# DEVELOPER COMMANDS
##############################################

install:
	$(PIP) install -r requirements-dev.txt  -r requirements.txt

lint:
	black src

test:
	$(PYTHON) -m pytest tests -vv --cov=eze --cov-branch --cov-report=term-missing --cov-report html:reports/coverage/cov_html --cov-report=xml:reports/coverage/coverage.xml --junitxml=reports/xunit/test-results.xml -o junit_family=xunit1 || true


all: install verify

.DEFAULT_GOAL := all
