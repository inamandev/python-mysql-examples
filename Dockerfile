FROM python:3.9
RUN pip install mysql-connector-python pandas
COPY main.py main.py
COPY helper.py helper.py
CMD ["python", "main.py"]