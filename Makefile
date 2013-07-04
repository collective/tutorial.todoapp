# convenience makefile to boostrap & run buildout
# use `make options=-v` to run buildout with extra options

python = python2.7
options =

all: docs tests

docs: docs/html/index.html

docs/html/index.html: README.rst docs/*.rst src/tutorial/todoapp/*.py \
		src/tutorial/todoapp/tests/*.py bin/sphinx-build
	bin/sphinx-build docs docs/html
	@touch $@
	@echo "Documentation was generated at '$@'."

bin/sphinx-build: .installed.cfg
	@touch $@

.installed.cfg: bin/buildout buildout.cfg buildout.d/*.cfg setup.py
	bin/buildout $(options)

bin/buildout: bin/python buildout.cfg bootstrap.py
	bin/python bootstrap.py -d
	@touch $@

bin/python:
	virtualenv -p $(python) --no-site-packages .
	@touch $@

tests: .installed.cfg
	@bin/test
	@bin/flake8 setup.py
	@bin/flake8 src/tutorial/todoapp
	@for pt in `find src/tutorial/todoapp -name "*.pt"` ; do bin/zptlint $$pt; done
	@for xml in `find src/tutorial/todoapp -name "*.xml"` ; do bin/zptlint $$xml; done
	@for zcml in `find src/tutorial/todoapp -name "*.zcml"` ; do bin/zptlint $$zcml; done

clean:
	@rm -rf .installed.cfg .mr.developer.cfg bin docs/html parts develop-eggs \
		src/tutorial.todoapp.egg-info lib include .Python

.PHONY: all docs tests clean
