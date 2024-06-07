# Flask Jumpstart

## Dev container

The _Flask Jumpstart_ app runs in a [dev container](https://containers.dev/).
Follow the instructions below to create and run the dev container on your machine.

1.  Install and start [Docker Desktop](https://www.docker.com/products/docker-desktop/).
1.  Install and open [PyCharm](https://www.jetbrains.com/pycharm/).
1.  In the PyCharm menu, choose _File > Remote Development > Dev Containers > New Dev Containers > From VCS Project_,
    then enter _git@github.com:initialcapacity/flask-jumpstart.git_ to [start the dev container](https://www.jetbrains.com/help/pycharm/connect-to-devcontainer.html#start_container_from_product)
    in PyCharm.

## Python application

Once your dev container is running, open a terminal in PyCharm (Alt/Option + F12) and follow the instructions below to
ensure your environment is ready.

1.  Run tests with [unittest](https://docs.python.org/3/library/unittest.html).
    ```shell
    python -m unittest
    ```

1.  Run the app with [flask](https://flask.palletsprojects.com).
    ```shell
    python -m jumpstart
    ```

1.  Curl the health endpoint and check that the app is healthy.
    ```shell
    curl -i localhost:5001/health
    ```
