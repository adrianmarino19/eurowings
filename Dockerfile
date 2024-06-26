# FROM python:3.10.6-buster

# COPY requirements.txt /requirements.txt
# COPY takeoff /takeoff
# COPY setup.py /setup.py

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# RUN pip install .

# CMD uvicorn takeoff.api.api:app --host 0.0.0.0 --port $PORT


FROM python:3.10.6-buster
EXPOSE 8080

COPY requirements.txt /requirements.txt
COPY takeoff /takeoff
COPY setup.py /setup.py

RUN mkdir data
COPY data/airport_coordinates.csv /data/airport_coordinates.csv

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install .

CMD uvicorn takeoff.api.api:app --host 0.0.0.0 --port $PORT
