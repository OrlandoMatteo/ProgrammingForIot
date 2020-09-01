FROM python:3
COPY sensor.py /
COPY settings.json /
COPY requirements.txt /
RUN pip3 install -r requirements.txt
CMD ["python3","./sensor.py"]