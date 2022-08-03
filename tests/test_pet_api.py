# import pytest
import requests

api_url = "https://petstore3.swagger.io/api/v3/"
pet_endpoint = api_url + "pet/"
user_endpoint = api_url + "user/"

headers = {"api_key": "9764e546-76ae-4f54-bc73-8f75a00bdb4d"}

pet_data = {
    "id": 1,
    "name": "doggie",
    "category": {
        "id": 1,
        "name": "Dogs"
    },
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}


def test_add_pet():
    print(pet_endpoint)
    response = requests.post(pet_endpoint, json=pet_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == pet_data["id"]


def test_get_pet_by_id():
    pet_id = 1
    response = requests.get(pet_endpoint + str(pet_id), headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == pet_id


def test_get_pet_by_id_not_found():
    pet_id = 100
    response = requests.get(pet_endpoint + str(pet_id), headers=headers)
    assert response.status_code == 404


def test_get_pet_by_id_invalid_id():
    pet_id = "invalid"
    response = requests.get(pet_endpoint + str(pet_id), headers=headers)
    assert response.status_code == 400


def test_find_pets_by_status():
    status = "available"
    response = requests.get(pet_endpoint + "findByStatus?status=" + status, headers=headers)
    assert response.status_code == 200
    assert response.json()[0]["status"] == status


def test_delete_pet():
    pet_id = 1
    response = requests.delete(pet_endpoint + str(pet_id), headers=headers)
    assert response.status_code == 200
