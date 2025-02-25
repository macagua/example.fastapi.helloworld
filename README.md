# example.fastapi.helloworld

<img src="./docs/_static/fastapi-framework.png" alt="FastAPI" width="40%" />

Building a *Hello World* application with FastAPI.


----


## Requirements

Please execute the following commands:

```sh
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install -y python3-dev python3-pip python3-virtualenv
$ sudo apt install -y git
$ git clone https://github.com/macagua/example.fastapi.helloworld.git fastapi-helloworld
$ cd ./fastapi-helloworld
$ virtualenv --python /usr/bin/python3 venv
$ source ./venv/bin/activate
$ pip3 install -U pip
$ pip3 install -r requirements.txt
```

This way, it has all the necessary requirements to execute
the example.

----


## Running

Please execute the following command:

```sh
$ fastapi dev main.py
```

Open a new terminal windows for testing the API using a HTTP client
as [curl](https://curl.se/) command.


----


## Make requests

The ``curl`` command allows you to quickly test an API from the terminal without
the need for having to download a specific application.


## request GET with response 200


```sh
$ curl -X GET http://127.0.0.1:8000/
```

The above command demonstrates how to perform a ``GET`` request to get the ``Hello World`` message.


----


## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.


----


## References

- [FastAPI](https://fastapi.tiangolo.com/).
- [First Steps - FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/).
