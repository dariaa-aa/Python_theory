import random

import pytest
import requests

base_url = 'https://restful-booker.herokuapp.com/booking'
auth_url = 'https://restful-booker.herokuapp.com/auth'
@pytest.fixture
def auth_token():
    data = {
    "username" : "admin",
    "password" : "password123"
}
    response = requests.post(auth_url, json=data)
    yield response.json()['token']
@pytest.fixture
def random_booking():
    return random.randint(1, 150)
@pytest.fixture
def create_booking():
    data = {
    "firstname" : "Dasha",
    "lastname" : "Podolskaia",
    "totalprice" : 20,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response = requests.post(base_url, json=data)
    yield response.json()['bookingid']

def test_get_random_booking_by_id(random_booking):
    response = requests.get(f'{base_url}/{random_booking}')
    # print(response.json())
    assert response.status_code == 200

def test_check_created_booking(create_booking):
    response = requests.get(f'{base_url}/{create_booking}')
    print(response.json())
    assert response.status_code == 200
@pytest.mark.slow
def test_change_booking(create_booking, auth_token):
    data = {
    "firstname" : "Dasha",
    "lastname" : "Podolskaia",
    "totalprice" : 20,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2024-01-01",
        "checkout" : "2024-02-01"
    },
    "additionalneeds" : "Lunch"
}
    token = {'Cookie': f'token = {auth_token}'}
    response = requests.put(f'{base_url}/{create_booking}', json=data, headers=token)
    assert response.status_code == 200
    response_2 = requests.get(f'{base_url}/{create_booking}')
    print(response_2.json())
    assert response_2.json()['additionalneeds'] == 'Lunch'
@pytest.mark.xfail
def test_partial_booking_update(create_booking, auth_token):
    data = {
        "firstname": "Daria"
    }
    token = {'Cookie': f'token = {auth_token}'}
    response = requests.patch(f'{base_url}/{create_booking}', json=data, headers=token)
    assert response.status_code == 200
    response_2 = requests.get(f'{base_url}/{create_booking}')
    print(response_2.json())

def test_detele_booking(create_booking, auth_token):
    token = {'Cookie': f'token = {auth_token}'}
    response = requests.delete(f'{base_url}/{create_booking}', headers=token)
    assert response.status_code == 201
    response_2 = requests.get(f'{base_url}/{create_booking}')
    assert response_2.status_code == 404