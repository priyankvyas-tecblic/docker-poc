# docker-poc
this django project is implemented with docker 

## setup docker
```
sudo apt-get update
sudo apt-get install docker
```
## how to install
```
git clone https://github.com/priyankvyas-tecblic/docker-poc.git
docker build -t docker_django .
docker run -p 8002:8002 docker_django
```
