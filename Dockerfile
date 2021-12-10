FROM python:3

# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY flaskr flaskr
COPY requirements.txt requirements.txt

RUN ls -al

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN flask --help

RUN flask --help

# tell the port number the container should expose
EXPOSE 5000

ENV FLASK_APP=/app/flaskr/app.py

# run the command
CMD ["flask", "run", "--host=0.0.0.0"]