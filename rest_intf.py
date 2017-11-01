#!/usr/bin/env python

from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route('/restpi/shutdown', methods=['GET'])
def shutdown():
    print "shutdown called"
    resp = Response(status = 200)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
