# access-key-checker
입력된 시간보다 오래된 AWS IAM Access Key를 찾아서 Slack 웹훅으로 전송해주는 어플리케이션

## Requirements (local)
```bash
python >= 3
```

## API Requests & Responses
### hello
인사말 출력
- request
```bash
GET /
```
- response
```bash
{"header": {"isSuccessful": true, "resultMessage": "Hello Access Key Checker!", "resultCode": 0}, "data": []}
```
### check
hour 파라미터를 기준으로 현재를 기준으로 N시간이 지난 Access Key를 전부 찾고 Slack으로 발송한 후에 응답으로 표시
- request
```bash
GET /check?hour=${hour}
# hour: 현재로부터 N시간 차이 (positive integer)
```
- response
```bash
{
  "header": {"isSuccessful": "성공/실패여부", "resultMessage": "성공/실패메세지", , "resultCode": "결과코드"},
  "data": ["hour(N) 시간 Access Key 리스트"]
}
# 결과코드: 0(성공), -1(실패)
```

## Development Running
```bash
pip install -r requirement.txt
export AWS_SECRET_ACCESS_KEY=${NEED_TO_SET_UP}
export AWS_ACCESS_KEY_ID=${NEED_TO_SET_UP}
export SLACK_WEBHOOK_URL=${NEED_TO_SET_UP}
export FLASK_ENV=development
export FLASK_APP=flaskr/app.py
flask run --host=0.0.0.0
# curl localhost:5000  
```

## Running Test
```bash
pytest
```

## Build & Push Container
```bash
# Login into prive
docker login
# Set ${TAG}
DOCKER_BUILDKIT=0 docker build -t ${TAG} .
docker push ${TAG}
```

## Running in docker
```bash
# copy sample docker-compose.yml
cp docker-compose.sample.yml docker-compose.yml
# set ${IMAGE}, ${AWS_ACCESS_KEY_ID}, ${AWS_SECRET_ACCESS_KEY}, ${SLACK_WEBHOOK_URL} in docker-compose.yml
docker-compose up -d
```

## Running in Kubernetes
```bash
# copy sample manifest.yaml
cp manifest.sample.yaml manifest.yaml
# set ${IMAGE}, ${AWS_ACCESS_KEY_ID}, ${AWS_SECRET_ACCESS_KEY}, ${SLACK_WEBHOOK_URL} in manifest.yaml 
kubectl apply -f manifest.yaml

# minikube 환경에서 접근할 경우
minikube service access-key-checker-service
```