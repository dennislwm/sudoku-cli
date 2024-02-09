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
	@flake8 --ignore=E231 sudoku/ tests/ benchmarks/

benchmark:
	@python benchmarks/benchmarks.py

run:
	@. ./bin/sudokurc.sh && sudoku_assert || exit 1
	@. ./bin/sudokurc.sh && time sudoku_fold $(puzzle)