import docker
from flask import Flask
from flask_limiter import Limiter
from flask_cors import CORS, cross_origin
from flask import request
from flask_limiter.util import get_remote_address
import base64
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["240 per day", "10 per hour"]
)

#client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')
client = docker.from_env()

@app.route("/scan", methods = ['POST'])
@cross_origin()
def scan():
    repository = request.form['repository']
    decodedRepository = repository.decode('base64')
    container = client.containers.run('autosec', command=decodedRepository, name="trial",detach=True)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


@app.route("/logs", methods = ['POST'])
@cross_origin()
def logs():
    containername = request.form['name']
    container =  client.containers.get(containername)
    containerLogs = container.logs()
    containerLogs = containerLogs.split("report...", 1)[1]
    return containerLogs
