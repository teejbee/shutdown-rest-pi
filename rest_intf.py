#!/usr/bin/env python

from flask import Flask
from flask import Response
from subprocess import call

app = Flask(__name__)

@app.route('/restpi/shutdown', methods=['GET'])
def shutdown():
    print "shutdown called"
    call("sudo nohup shutdown -h now", shell=True)
    resp = Response("OK Sir, I will shutdown now!", status = 200)
    return resp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
