from flask import Flask

app = Flask(__name__)

# API Route
@app.route("/ParseFile")
def parseFile():
    return {"categories": ["Test1", "Test2"]}

if __name__ == "__main__":
    app.run(debug=True)

#Run with - python flask-server/server.py