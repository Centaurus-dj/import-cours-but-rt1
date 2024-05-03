FROM python:3.12

LABEL maintainer="Alexis Opolka <support@alexis-opolka.dev>"

COPY flask-containerized.py /

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y \
  iproute2

RUN pip install --no-cache-dir --upgrade pip && \
  pip install --no-cache-dir flask

EXPOSE 5000/tcp
EXPOSE 5000/udp
EXPOSE 80/tcp
EXPOSE 80/udp

CMD ["python3", "/flask-containerized.py"]