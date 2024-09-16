# Test task
Python [Django] test task
Develop a Django REST-Api for Event Management
The primary goal of this task is to create a Django-based REST-Api that manages
events (like conferences, meetups, etc.). The application will allow users to create,
view, update, and delete events. It should also handle user registrations for these
events.

Key Requirements
- Design an Event model with fields such as title, description, date, location,
and organizer.    [Done]
- Implement CRUD (Create, Read, Update, Delete) operations for the Event
model.   [Done]
- Basic User Registration and Authentication.   [Done]
- Event Registration   [Done]
- API documentation   [Done]
- Docker   [Done]
- Readme file   [Done]

Bonus Points
- Implement an advanced feature like event search or filtering.   [In progress]
- Add a feature for sending email notifications to users upon event registration.   [In progress]
  
# EventManagement
This is an API for event management, you can both register for existing events and create your own. To register for an event, you only need a name and email, to create your own event, you need to register in the API.




## Installation
Clone project

```bash
  git clone https://github.com/seures-dev/EventManagement
  cd EventManager
```

Install by docker

```bash
  //Build image
  docker build -t <image_name> .
```
```
  //Create container 
  docker run -d -p <local_port>:8000 --name <container_name> <image_name> 
```

Local install

```bash
  //Create and activate environment
  python3 -m venv venv

  source venv/bin/activate
```
```
  //Install requirements

  pip install -r requirements.txt

```
```
  //Start server
  cd EventManager

  python3 manage.py runserver
```
Create superuser
```
  //If you use docker, connect to container by shell
    docker exec -it <container_name>  /bin/bash
```
```
  cd EventManager
```
```
  python3 manage.py createsuperuser
```
Write superuser username, email and password 

## Swager

```http
  http://${host}:${port}/swagger/
```


## API Reference

#### Get all events

```http
  GET /events/
```


### Events CRUD
*All CRUD except read need Auth token*

In headers:

| Header | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | Bearer token for authentication |

In parameter:
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `event_id`      | `string` | **Required**. Event name |

#### Read
```http
  GET /events/${event_id:int}
```
#### Delete
```http
  DELETE /events/${event_id:int}
```

#### Create
```http
  POST /events/
```
Required body:
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. Event name |
| `description`      | `string` | **Required**. Event description |
| `date`      | `string` | **Required**. The date on which the event is planned  |
| `location`      | `string` | **Required**. Event location |


#### Update
```http
  PATCH /events/${event_id:int}
```


Required body:
| Keys | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` |  Event name |
| `description`      | `string` | Event description |
| `date`      | `string` |  The date on which the event is planned  |
| `location`      | `string` |  Event location |



### Registration on event
```http
  POST /events/${event_id:int}
```
Required body:
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Guest name |
| `email`      | `string` | **Required**. Guest email |

### User registration and authentication
#### Registration
```http
  POST /register/
```
Required body:
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. Username |
| `email`      | `string` | **Required**. User email |
| `password`      | `string` | **Required**. User password |
| `password2`      | `string` | **Required**. Repeat user password |

#### Authentication(Login)
```http
  POST /login/
```
Required body:
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. Username |
| `password`      | `string` | **Required**. User password |


