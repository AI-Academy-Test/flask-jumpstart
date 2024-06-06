# Flask Jumpstart

## Dev container

The _Flask Jumpstart_ app runs in a [dev container](https://containers.dev/).
Follow the instructions below to create and run the dev container on your machine.

1.  Install and start [Docker Desktop](https://www.docker.com/products/docker-desktop/).
1.  Follow [Jetbrains' instructions](https://www.jetbrains.com/help/pycharm/connect-to-devcontainer.html#start_container_from_product)
    to start the dev container in [PyCharm](https://www.jetbrains.com/pycharm/) (be sure to choose the
    _From VCS Project_ option).

## Python application

Once your dev container is running, follow the instructions below to ensure your environment is ready.

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
