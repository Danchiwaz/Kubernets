FROM python:3.9-slim

#set the working directory 
WORKDIR /app

COPY . /app

# install the python dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# make the port 5000 available to the outside world this container
EXPOSE 5000

# run the app.py when the container launches

CMD ["python", "app.py"]