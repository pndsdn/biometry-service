FROM python:3.9
LABEL maintainer="saa020403@gmail.com"
LABEL version="1.0.0"
ARG tmp_folder=/usr/src/tmp/
RUN mkdir $tmp_folder
WORKDIR /usr/src/app/
COPY . .
RUN pip install --cache-dir=$tmp_folder -r requirements.txt
EXPOSE 8888
CMD ["python", "snp_server.py"]