install:
	pip install  pip;
	pip install -r requirements.txt
lint:
	pylint --disable=C,R app.py
test:
	python -m pytest -vv --cov=calc py_test.py