FROM python:3
ADD sensor.py /
ADD settings.json /
ADD requirements.txt /
RUN pip3 install -r requirements.txt
CMD ["python3","./sensor.py"]