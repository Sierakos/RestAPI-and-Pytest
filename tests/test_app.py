import pytest
import requests
from uuid import uuid4
from libraries.shortcuts_pytest import *

def test_can_connect_to_home_page():
    response = get_data("")
    assert response.status_code == 200

def test_can_get_all_data():
    # delete data
    delete_data()

    # create items
    n = 5
    names = []
    get_names = []

    brands = []
    get_brands = []
    for _ in range(n):
        create_response = create_data()
        assert create_response.status_code == 200
        names.append(create_response.json()["name"])
        brands.append(create_response.json()["genree"])

    # get items and check status code
    get_response = get_data("get-all-items/")
    assert get_response.status_code == 200

    # check names and brands
    for i in range(n):
        get_names.append(get_response.json()[f"{i+1}"]["name"])
        get_brands.append(get_response.json()[f"{i+1}"]["genree"])

    assert names == get_names
    assert brands == get_brands

    # delete data
    delete_data()
    
    # verify that all items have been deleted
    verify_response = get_data("get-all-items/")
    assert verify_response.status_code == 200
    assert len(verify_response.json()) == 0

def test_can_get_data_by_id():
    # delete data
    delete_data()

    # create items
    n = 3
    for _ in range(n):
        create_response = create_data()
        assert create_response.status_code == 200

    # get items and check status code
    for item_id in range(n):
        get_response = get_data(f"get-item/{item_id+1}")
        assert get_response.status_code == 200
        
    # delete data
    delete_data()

    # verify that all items have been deleted
    verify_response = get_data("get-all-items/")
    assert verify_response.status_code == 200
    assert len(verify_response.json()) == 0

def test_can_get_data_by_name():
    # delete data
    delete_data()

    # create items
    n = 3
    names = []
    for _ in range(n):
        create_response = create_data()
        assert create_response.status_code == 200
        names.append(create_response.json()["name"])

    # get items and check status code
    for i in range(n):
        get_response = get_data(f"get-by-name?name={names[i]}")
        assert get_response.status_code == 200
        
    # delete data
    delete_data()

    # verify that all items have been deleted
    verify_response = get_data("get-all-items/")
    assert verify_response.status_code == 200
    assert len(verify_response.json()) == 0
    