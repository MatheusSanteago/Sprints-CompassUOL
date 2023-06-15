# Desafio
#### Parte 1 - Upar arquivos brutos

1) Implementar código Python: [Script](https://github.com/MatheusSanteago/Sprints-CompassUOL/blob/main/Sprint7/Desafio1/main.py)


2) Criar container Docker com um volume para armazenar os arquivos CSV e executar processo Python implementado
    ### Comandos utilizados.

    > **docker build . -t desafio**

    > **docker container run -it -v desafio:/home desafio**
    
    > **docker cp C:\Desafio 875:/home**
    
    > **docker start 875**
    
    > **docker exec -it 875 /bin/bash**
    
    > **docker volume create desafio**
    
    >**aws configure sso**
    
    >**aws configure**
    
    **[Dockerfile utilizado](https://github.com/MatheusSanteago/Sprints-CompassUOL/blob/main/Sprint7/Desafio1/Dockerfile)**
    
    
3) Executar localmente o container docker para realizar a carga dos dados ao S3
   > **python3 main.py**


## Amazon S3

<img src="https://github.com/MatheusSanteago/Sprints-CompassUOL/blob/main/Sprint7/Desafio1/s3PathMovies.png">
<img src="https://github.com/MatheusSanteago/Sprints-CompassUOL/blob/main/Sprint7/Desafio1/s3PathSeries.png">
