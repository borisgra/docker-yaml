# start by pulling the python image
# 18 MB
#FROM python:3.12-rc-alpine3.17
# 52 MB - need for paramiko
FROM python:3.11-slim

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

EXPOSE 5003

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["hook.py"]

# sudo docker image build -t borisgra/webhook:1.0 .
# sudo docker image build --progress=plain --no-cache -t borisgra/webhook:1.0 .
# sudo docker login -u borisgra
# sudo docker push borisgra/webhook:1.0