FROM python:3.9.2-slim-buster
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git wget pv jq python3-dev ffmpeg mediainfo
RUN apt-get install neofetch wget -y -f
RUN pip3 install --upgrade pip setuptools
RUN git clone https://github.com/Rajbhaiya/SnowCompressorBot /app
WORKDIR /app 

RUN python3 -m pip install --no-cache-dir -r requirements.txt
CMD ["bash","run.sh"]
