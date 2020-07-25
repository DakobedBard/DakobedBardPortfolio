# Simple Python Flask Dockerized Application#

Build the image using the following command

```bash
$ docker build -t simple-flask-app:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 5000:5000 simple-flask-app
```

The application will be accessible at http:127.0.0.1:5000 or if you are using boot2docker then first find ip address using `$ boot2docker ip` and the use the ip `http://<host_ip>:5000`

snotel route..

http://127.0.0.1:5000/snotel/trinity/20140101/20140104


Elastic Beanstalk

eb init -p python-3.6 snotel-flask --region us-west-2

Run eb init again to select .pem for ssh

eb open -> 
eb terminate flask-env




