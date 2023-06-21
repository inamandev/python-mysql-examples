FROM python:3.9
COPY main.py main.py
RUN pip install mysql-connector-python pandas
CMD ["python", "main.py"]