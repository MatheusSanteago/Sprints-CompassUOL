FROM ubuntu
RUN apt update && apt upgrade -y
RUN apt install curl mlocate default-jdk -y
RUN apt install wget nano -y
RUN wget https://dlcdn.apache.org/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3.tgz
EXPOSE 80