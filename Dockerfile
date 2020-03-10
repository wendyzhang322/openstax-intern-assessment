FROM python:3
ADD /code/read_greetings.py /
ADD greetings.xml /
CMD ["python", "./read_greetings.py"]
