FROM python:3
ADD device.py /
ADD settings.json /
ADD requirements.txt /
RUN pip3 install -r requirements.txt
CMD ["python3","./device.py"]