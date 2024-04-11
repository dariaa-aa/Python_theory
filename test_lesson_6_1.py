import random

import requests
import pytest

base_url = "https://petstore.swagger.io/v2"
pet_url = "/pet"
pet_id = random.randint(1, 10000)

# def test_get_pet_by_id():
#     response = requests.get(f'{base_url}{pet_url}/5')
#     assert response.status_code == 200
#     print(response.json())


def test_create_pet():
    with open("id", "w", encoding="utf-8") as f:
        f.write(f"{pet_id}")
    payload = {
            "id": pet_id,
            "category": {
                "id": 2,
                "name": "Dasha"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 5,
                    "name": "string"
                }
            ],
            "status": "available"
        }
    response = requests.post(f'{base_url}{pet_url}', json=payload)
    assert response.status_code == 200
    print(response.json())
    print("=====================================")
    response1 = requests.get(f'{base_url}{pet_url}/{pet_id}')
    print(response1.json())


def test_update_pet_by_id():
    with open("id", "r", encoding="utf-8") as f:
        id = f.readline().strip()
    payload = {
        "id": id,
        "category": {
            "id": 2,
            "name": "Dasha Dasha"
        },
        "name": "carry",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 5,
                "name": "string"
            }
        ],
        "status": "available"
    }

    response = requests.put(f"{base_url}{pet_url}", json=payload)
    assert response.status_code == 200
    print("=====================================")
    print(response.json())
    print("=====================================")
    response1 = requests.get(f'{base_url}{pet_url}/{id}')
    print(response1.json())

def test_delete_pet_by_id():
    with open("id", "r", encoding="utf-8") as f:
        id = f.readline().strip()
    response = requests.delete(f"{base_url}{pet_url}/{id}")
    assert response.status_code == 200
    print(response.json())
    print("=====================================")
    response1 = requests.get(f"{base_url}{pet_url}/{id}")
    print(response1.json())