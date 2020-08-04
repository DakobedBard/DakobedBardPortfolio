FROM  tensorflow/tensorflow:latest-gpu-py3

RUN mkdir results
RUN pip install keras
RUN pip install Pillow
RUN pip install awscli
RUN pip install --upgrade boto3
RUN apt-get -qq update && apt-get install -y build-essential \
    libssl-dev groff \
    && rm -rf /var/lib/apt/lists/*
RUN python -m pip install ecs-logging
RUN mkdir mddarr

#COPY download_vgg19.py download.py
#RUN python3 download.py
#COPY tftest.py tftest.py
#COPY img/style.jpg img/style.jpg
#COPY img/sword2.jpg img/sword2.jpg
COPY uploadS3.py uploadS3.py
COPY entrypoint.sh entrypoint.sh
COPY transfer.py transfer.py
ENTRYPOINT ["bash", "entrypoint.sh"]
#RUN python3 tftest.py  sword2.jpg    style.jpg results/my_result
#RUN pip install -r requirements.txt
#RUN python3 copy.py
