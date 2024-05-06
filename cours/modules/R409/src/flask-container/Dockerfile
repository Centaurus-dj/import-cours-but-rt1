from python:3.12

maintainer Alexis Opolka <support@alexis-opolka.dev>

COPY flask-uncontainerized.py /

RUN pip install --no-cache-dir --upgrade pip && \
  pip install --no-cache-dir flask

EXPOSE 5000/tcp
EXPOSE 5000/udp

CMD ["python3", "/flask-uncontainerized.py"]