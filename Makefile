install:
	@rm -rf *.egg-info
	@pip install --editable .

requirements:
	@pip install -r requirements.txt

test:
	@rm -f .coverage
	@coverage run --source=sudoku/ -m unittest discover -s tests/
	@coverage report -m
	@flake8 cli.py sudoku/