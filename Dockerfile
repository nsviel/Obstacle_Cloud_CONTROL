FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive
ENV TZ Europe/Paris

# Install dependancy packages
RUN mkdir app \
    && apt update \
    && apt install -y \
    python3 python3-pip python3-pcapy python3-scapy libiperf0 \
    libx11-6 libgl1-mesa-glx libgl1-mesa-dri \
    && pip3 install dearpygui speedtest-cli dhcppython pandas psutil \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && apt autoremove -y

# Program parameters
COPY . /app/controlium
WORKDIR /app/controlium

# Open port
EXPOSE 321
EXPOSE 322

# Final command
CMD [ "python3", "main.py"]
