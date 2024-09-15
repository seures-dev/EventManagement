# Event Management
This is an API for event management, you can both register for existing events and create your own. To register for an event, you only need a name and email, to create your own event, you need to register in the API.




## Installation
Clone project

```bash
  git clone https://github.com/seures-dev/EventManagement
  cd EventManager
```

Docker

```bash
  //Build image
  docker build -t <image_name> .

  //Create container 
  docker run -d -p <local_port>:8000 --name <container_name> <image_name> 
```

Local install

```bash
  //Create and activate environment
  python3 -m venv venv

  source venv/bin/activate

  //Install requirements

  pip install -r requirements.txt

  //Start server

  cd EventManager

  python3 manage.py runserver
```
Create superuser
```
  //If you use docker, connect to container by shell
    docker exec -it <container_name>  /bin/bash

  cd EventManager

  python3 manage.py createsuperuser

  Write superuser username, email and password 
```



