test:
	@coverage run --source=sudoku/ -m unittest discover -s tests/
	@coverage report -m