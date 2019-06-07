# docker build --tag zeitonline/github-vulnerability-exporter:PACKAGEVERSION-DOCKERVERSION .
FROM python:3-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-deps -r requirements.txt
ENTRYPOINT ["github_vulnerability_exporter"]
