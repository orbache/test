# Created_by Evyatar Orbach
import docker
from flask import Flask, render_template, render_template_string

app = Flask(__name__)


@app.route('/')
def ps():
    list_containers = []
    client = docker.from_env()
    for container in client.containers.list():
        list_containers.append(container.id)
        print(container.id)
    return render_template('data.html', data=list_containers)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
