#DevOps Monitoring App

A simple Python Flask application that shows system information (like hostname, CPU, memory) via a `/info` endpoint.

#Features
- Built with Flask
- Dockerized
- `/info` route returns JSON with system metrics
- Tested with Python `unittest`
- CI/CD pipeline using GitHub Actions

#Run Locally with Docker
```bash
docker build -t devops-monitoring-app .
docker run -d -p 5000:5000 devops-monitoring-app
