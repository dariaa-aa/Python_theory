import pytest
import requests

# class Calculator:
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#     @staticmethod
#     def sub(a, b):
#         return a - b
#
#     @staticmethod
#     def div(a, b):
#         return a / b
# @pytest.fixture
# def calc():
#     return Calculator()
#
# def test_add(calc):
#     assert calc.add(4, 5) == 9
#
# def test_sub(calc):
#     assert calc.sub(10, 5) == 5
# @pytest.mark.slow
# @pytest.mark.smoke
# def test_div(calc):
#     assert calc.div(10, 5) == 2
#
# @pytest.mark.skip('Will be fixed later')
# @pytest.mark.xfail
# def test_div_zero(calc):
#     assert calc.div(10, 0) == None

base_url = 'https://restful-booker.herokuapp.com/booking'
auth_url = 'https://restful-booker.herokuapp.com/auth'

def create_booking(fname, lname):
    payload = {
    "firstname" : fname,
    "lastname" : lname,
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

    response = requests.post(base_url, json=payload)
    return response.json()

def get_booking_by_id(id_):
    url = f'{base_url}/{id_}'
    response = requests.get(url)
    return response.json()

# print(get_booking_by_id(2))
@pytest.fixture
def token():
    data = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(auth_url, json=data)
    return response.json()['token']

# print(create_token())

def test_create_booking():
    fname = 'Dasha'
    lname = 'Podolskaia'

    booking = create_booking(fname=fname, lname=lname)
    id_ = booking['bookingid']

    new_booking = get_booking_by_id(id_)

    assert new_booking['firstname'] == fname and new_booking['lastname'] == lname

def test_create_and_patch(token):
    fname = 'Dasha'
    lname = 'Podolskaia'
    new_fname = 'Pasha'
    new_lname = 'Poopkin'

    booking = create_booking(fname=fname, lname=lname)
    id_ = booking['bookingid']

    headers = {'Cookie': f'token={token}'}

    new_data = {
        "firstname": new_fname,
        "lastname": new_lname
    }

    response = requests.patch(f'{base_url}/{id_}', json=new_data, headers=headers)
    assert response.json()['firstname'] == new_fname and response.json()['lastname'] == new_lname