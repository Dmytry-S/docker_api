FROM python:3.8-slim-buster
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . . 
CMD [ "pytest", "tests/test_api_tests.py" ]

