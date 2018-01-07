install: clean
	@pip install --editable .

requirements:
	@pip install -r requirements.txt

test: clean
	@coverage run --source=sudoku/ -m unittest discover -s tests/
	@coverage report -m
	@flake8 sudoku/

clean:
	@rm -rf *.egg-info
	@rm -f .coverage