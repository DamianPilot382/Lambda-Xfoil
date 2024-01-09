from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
    ret = os.popen("xfoil").read()
    print(ret)
    return ret


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)