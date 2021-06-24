# docker build --tag eu.gcr.io/zeitonline-210413/github-vulnerability-exporter:PACKAGEVERSION-DOCKERVERSION .
FROM python:3-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-deps -r requirements.txt
ENTRYPOINT ["github_vulnerability_exporter"]
