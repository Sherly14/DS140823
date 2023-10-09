from flask import Flask

app = Flask(__name__)

@app.route("/bharati")
def greet():
    return {"data":"Hello"}

app.run()