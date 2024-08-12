import pytest
from pip._vendor import requests

base_url ="https://reqres.in/"


def test_get_requiest():
    header_type = {'Content-type' : 'Application/json'}
    resp = requests.get(str(base_url+'/api/products/3'),headers = header_type)
    print(resp.headers)
    assert resp.status_code == 404

#get_requiest(base_url)    