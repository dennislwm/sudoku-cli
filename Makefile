install:
	@rm -rf *.egg-info
	@pip install --editable .

requirements:
	@pip install -r requirements.txt

compile:
	@rm -rf dist/
	@python setup.py sdist

test:
	@rm -f .coverage
	@coverage run --source=sudoku/ -m unittest discover -s tests/
	@coverage report -m
	@flake8 sudoku/

benchmark:
	@python benchmarks/benchmarks.py