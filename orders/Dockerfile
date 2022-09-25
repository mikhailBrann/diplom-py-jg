FROM python:3.7-alpine
# set work directory
WORKDIR ./orders
# copy project
COPY ./ ./orders/

RUN cd ./orders
RUN pip install --upgrade pip
RUN pip install -r ./orders/requirements.txt
