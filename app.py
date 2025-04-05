from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hey baby, your CI/CD pipeline is working! 💖 Hey madhu the rockstar if you are seeing this succefully then let me tell you that i am  currently hosted on an online cloud platform by railwayapp deployed live using the CICI pipeline)"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8080))  # default to 8080
    app.run(host='0.0.0.0', port=port)