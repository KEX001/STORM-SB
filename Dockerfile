FROM nikolaik/python-nodejs:python3.10-nodejs19
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app/
COPY . /app/
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN chmod +x start.sh
CMD ["bash", "start.sh"]
