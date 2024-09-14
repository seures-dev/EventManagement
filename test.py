import requests
import json

def test_register_user():
    data = {
            'username': "test_user1",
            'email': "test_user1@example.com",
            'password': "test_passs",
            'password2': "test_passs",
    }
    response_user_register = requests.post('http://127.0.0.1:8000/register/', data=data)
    response_json = response_user_register.json()
    token = response_json['token']
    return token

def test_login_user():
    data = {
            'username': "test_user1",
            'password': "test_passs",
            }
    response = requests.post('http://127.0.0.1:8000/login/', data=data)
    print(response.json())
    token = response.json()['token']
    return token


def test_create_event(token):
    header = {
        'Authorization': f'Token {token}'
    }
    new_event_data = {
        "title": "test_event",
        "description": "test event",
        "date": "2024-09-19",
        "location": "vinnitsya",
    }
    create_response = requests.post('http://127.0.0.1:8000/events/', headers=header, data=new_event_data)
    event_id = create_response.json()['id']
    print(f'Create event: \n{create_response.json()}')
    return event_id

def test_update_event(token, event_id):
    header = {
        'Authorization': f'Token {token}'
    }
    new_event_data = {
        "title": "test_1_event",
        "description": "test_2_event",
        "date": "2024-09-29",
        "location": "Lviv",
    }
    response = requests.patch('http://127.0.0.1:8000/events/', headers=header, data=new_event_data)
    print(f'Update event: \n{response.json()}')

def test_delete_event(token , event_id):
    if token is None:
        return
    header = {
        'Authorization': f'Token {token}'
    }
    response_delete = requests.delete(f'http://127.0.0.1:8000/events/{event_id}/' , headers=header)
    if response_delete.status_code == 204:
        print(f'Delete event: {event_id}')
    else:
        print(f'Delete event error: \n{response_delete.status_code}')
        print(f'{response_delete.json()}')

def test_registration_on_event(event_id):
    for i in range(5):
        data = {'email':f'string{i}@string.com', 'name':'string'}
        response_delete = requests.post(f'http://127.0.0.1:8000/events/{event_id}/registration/' , data=data)
        print(f'Registration on event: \n{response_delete.json()}')

if __name__ == '__main__':
    # token = test_login_user()
    # event = test_create_event(token)
    test_registration_on_event(7)
    # test_delete_event('5d6d6226f9664677008c06d7bbe7b161568e3034', 3)