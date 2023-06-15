docker build . -t desafio
docker volume create desafio
docker container run -it --name desafio-part1 -itd desafio ---  docker container run -it -v desafio:/home desafio
docker cp C:\Desafio 875:/home 
docker start 875
docker exec -it 875 /bin/bash
aws configure sso
aws configure
python3 main.py