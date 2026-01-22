FROM ubuntu:20.04

RUN apt update && apt install -y python3 python3-pip
WORKDIR /mission
COPY . .
RUN pip3 install -r requirements.txt

CMD ["python3", "scripts/mission.py"]