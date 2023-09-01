# fastapi-postgres

도커를 활용해 fastapi 서버를 구축

db는 postgres 사용

## install

1. docker에서 postgres 이미지 받아 실행

2. Dockerfile을 활용하여 fastapi 실행 

```
docker build -t ws .
```

3. fastapi 컨테이너에 붙어서 db 연결 확인

```
docker exec -it ws sh
apk add postgresql-client
psql -h locahost -U postgres
```

4. 웹에 접속 해 확인 127.0.0.1:8000