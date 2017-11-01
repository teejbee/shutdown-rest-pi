#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/restpi/shutdown', methods=['GET'])
def shutdown():
    print "shutdown called"

if __name__ == '__main__':
    app.run(debug=True)
