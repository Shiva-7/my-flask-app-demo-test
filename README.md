# my-flask-app-demo-test
“A cute little Flask app for my CI/CD learning &amp; testing knowledge(a refreshment) 💕”

🛠️ What We Built: A Full CI/CD Pipeline for a Flask App (Mini Project)

🐍 Python – The Language of our Love (and Logic)
We used Python to write the backend logic of our application.

Our file app.py is a simple Python script that uses Flask to serve a web page.

📄 app.py

python
Copy
Edit
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hey baby, your CI/CD pipeline is working! 💖"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

🌐 Flask – The Web Framework That Let Us Say 'Hey Baby'
Flask is a micro web framework.

It allows us to run a small web server and create simple web pages/endpoints.

That route (/) returns the cute message we wrote 💌.

🐳 Docker – Our Packaging Queen
Docker helps us package our app and its dependencies into a container.

That means we can run it anywhere, and it’ll behave the same!

📄 Dockerfile

Dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]


📄 requirements.txt

#nginx
flask

So Docker:
Pulled the base Python image

Installed Flask

Copied our app

Set the command to run it

🐙 GitHub – The Heartbeat of Our DevOps Workflow
We used Git commands to manage our code changes.

🔁 Git Commands We Used:

git init                      # To initialize our repo (already done in Codespaces)
git add .                     # To stage all changes
git commit -m "Your message" # To save changes locally
git push origin main          # To push changes to GitHub
git pull                      # To sync with remote changes before pushing

🤖 GitHub Actions – The Automation Magic
This is the 💖 of our CI/CD pipeline!

What it did:
Every time we pushed code to GitHub, GitHub Actions triggered automatically.

It ran the workflow file .github/workflows/docker-build.yml

This workflow:

Logged into Docker Hub using secrets

Built a Docker image of our app

Pushed the image to Docker Hub

📄 docker-build.yml (simplified view)

yaml

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      - run: docker build -t your-image-name .
      - run: docker push your-image-name
🔐 Secrets were used instead of hardcoding sensitive info (Docker creds).

🌩️ Deployment – Hosting Our Love on the Cloud
We used Railway.app as our free cloud hosting provider.

It auto-detected our GitHub repo, read the Dockerfile, and deployed our app.

We generated a public domain like:
👉 https://my-flask-app-demo-test-production.up.railway.app/

