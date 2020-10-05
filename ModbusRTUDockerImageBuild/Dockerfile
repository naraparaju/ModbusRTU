# set base image (host OS)
#FROM python:3.8
FROM python:3.7-alpine

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY ./ModbusRTUMaster.py /app

# command to run on container start
#CMD [ "python3", "-u", "./ModbusRTUMaster.py", "port")
ENTRYPOINT  ["python3", "-u", "./ModbusRTUMaster.py"]