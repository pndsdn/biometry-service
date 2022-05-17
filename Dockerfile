FROM python:3.9
LABEL maintainer="saa020403@gmail.com"
LABEL version="1.0.0"
WORKDIR /usr/src/app/
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8888
CMD ["python", "snp_server.py"]