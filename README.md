# FastAPI and MongoDB 

A simple starter for building RESTful APIs with FastAPI and MongoDB. 

## Features

+ Python FastAPI backend.
+ MongoDB database.

## Using the applicaiton

To use the application, follow the outlined steps:

1. Clone this repository and create a virtual environment in it:

```console
$ python3 -m venv venv
```

3. You also need to start your mongodb instance either locally or on Docker as well as create a `.env` file. See the sample below for configurations.

```console
MONGO_URL=<url>
```


4. Start the application:

```console
python -m uvicorn server:app --reload
```


![FastAPI](https://github.com/PremKarira/CRUD_users/blob/main/1.png)



## License

This project is licensed under the terms of MIT license.