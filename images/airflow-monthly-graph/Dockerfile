FROM python:3.10

COPY monthly-graph.py requirements.txt /
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "monthly-graph.py"]
