.PHONY: clean install_deps test build all

clean:
	pyb clean

install_deps:
	python -m pip install -r requirements.txt

test:
	pyb run_unit_tests

build:
	pyb publish

all: clean install_deps test build
