#Download Python-Alpine based image from DockerHub and use it
FROM python:3.9-alpine
MAINTAINER brzozka  brzozka108@gmail.com

WORKDIR /app

#Copy the dependencies file to the working directory
COPY requirements.txt .
#COPY test_requirements.txt .

#Install the dependencies
RUN pip install -r requirements.txt
#RUN pip install -r test_requirements.txt


COPY service/ ./service
COPY app.py .
#Run the container
CMD [ "python", "./app.py" ]