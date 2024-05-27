FROM debian:latest
RUN apt-get update && \
    apt-get install -y stress
ENTRYPOINT [ "stress" ]
CMD ["-t", "30", "--cpu", "10"]