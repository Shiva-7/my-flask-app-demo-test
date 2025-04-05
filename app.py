from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hey baby, your CI/CD pipeline is working! 💖 with help of ChatGPT + Shiva love you mittu"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8080))  # default to 8080
    app.run(host='0.0.0.0', port=port)