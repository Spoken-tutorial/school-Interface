SHELL := /bin/bash

flake8 :
	@git ls-files '*.py' | \
		egrep -v '^docs/|/migrations/' | \
		xargs -r flake8 --statistics
