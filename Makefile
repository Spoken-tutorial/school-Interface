SHELL := /bin/bash

flake8 :
	find * \( -name docs -o -name env -o -name migrations \) -prune -o -type f -name \*.py -print \
		| sort \
		| xargs flake8 --statistics
