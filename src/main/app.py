from flask import Flask, request ,render_template
from history import *
from os.path import abspath
import config
from repo_tester import *
app = Flask(__name__)

# Database of builds
history = None

@app.route("/", methods = ['GET','POST'])
def hello():

    data = request.get_json(silent=True)# Load JSON data sent with POST request
    exit_code = repo_test(data)
    print("Exit code is: ")
    print(exit_code)
    return render_template('index.html', data=data)


def main():
    global history
    config.init()
    history = History(config.mongo_database_name, config.mongo_ip, config.mongo_port, config.mongo_user, config.mongo_pass)

if __name__ == '__main__':
    app.run(debug = True, port=8080)
    #main()
