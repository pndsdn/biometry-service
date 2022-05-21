FROM python:3.9
WORKDIR /usr/src/app/
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8888
CMD ["python", "snp_server.py"]