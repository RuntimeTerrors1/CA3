install:
	pip install -r requirements.txt
lint:
	pylint --disable=C,R app.py
test:
	python -m pytest -vv --cov=hello py_test.py