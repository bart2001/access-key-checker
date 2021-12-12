FROM python:3.9

# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY flaskr flaskr
COPY requirements.txt requirements.txt

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt


ENV FLASK_APP="/app/flaskr/app"
ENV FLASK_ENV="production"

# run the command
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]