FROM python
COPY . /app
WORKDIR /appworkdir
RUN pip3 freeze > requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
