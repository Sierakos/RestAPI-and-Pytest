import pytest
import requests
from uuid import uuid4
from .setup_endpoint import ENDPOINT

def get_data(url: str):
    """
    get data from specific url
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    get_data usage:
        >>> get_data("dummy-url/")

    this command is the same like below:
        >>> requests.get(ENDPOINT + "dummy-url/")

    leave blank string for home page like:
        >>> get_data("")
    """

    return requests.get(ENDPOINT + str(url))



def create_data():
    """
    create item with random name and brand
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    payload = {
            "name": "book: " + str(uuid4()),
            "author": "author: " + str(uuid4()),
            "year": 1999,
            "genree": "genree: " + str(uuid4())
        }
    return requests.post(ENDPOINT + "create-item/", json=payload)


def update_name_data_by_id(item_id: int, name: str):
    """
    update item with random name
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    update_name_data_by_id usage:
        >>> update_name_data_by_id(1, "dummy name")

    this command is the same like below:
        >>> payload = {"name": "dummy name"}
        >>> requests.put(ENDPOINT + f"{1}", json=payload)
    """
    payload = {
        "name": name
    }
    return requests.put(ENDPOINT + f"update-item/{item_id}", json=payload)


def delete_data():
    """
    cleanup data from api
    ~~~~~~~~~~~~~~~~~~~~~
    """ 

    try:
        response = get_data("get-all-items/")
        n = len(response.json())
        for item_id in range(n):
            delete_response = requests.delete(ENDPOINT + f"delete-item/{item_id+1}")
            assert delete_response.status_code == 200
    except:
        pass