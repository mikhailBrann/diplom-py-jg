FROM python:3.8-alpine
# set work directory
WORKDIR ./orders
# copy project
COPY ./ ./orders/

RUN cd ./orders
RUN pip3 install --upgrade pip
RUN pip3 install -r ./orders/requirements.txt
