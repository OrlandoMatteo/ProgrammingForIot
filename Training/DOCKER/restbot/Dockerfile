FROM python:3.7-alpine
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 80
CMD ["python3","./bot.py"]