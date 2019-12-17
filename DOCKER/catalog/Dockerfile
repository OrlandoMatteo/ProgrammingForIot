FROM python:3
ADD catalog.py /
ADD requirements.txt /
EXPOSE 80
RUN pip3 install -r requirements.txt
CMD ["python3","./catalog.py"]
