from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert
import re

def test_list_users():
    res = api.list_users()
    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema((res.json))

    assert res.headers['Cache-Control'] == 'max-age=14400'

def test_single_users_not_found():
    res = api.single_user_not_found()

    assert res.status_code == HTTPStatus.NOT_FOUND
#    Assert.validate_schema((res.json))

def test_single_users():
    res = api.single_user()
    res_body = res.json()

    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema(res_body)

    assert res_body['data']['first_name'] == 'Janet'
    assert re.fullmatch(r'\w[a-z]{5}', res.body["data"]["Last_name"],res.json()['id'])
    assert re.fullmatch(r'\w[a-z]+', res.body["data"]["Last_name"], res.json()['id'])
    assert re.fullmatch(r'\w+', res.body["data"]["Last_name"], res.json()['id'])
    assert re.fullmatch(r'.+', res.body["data"]["Last_name"], res.json()['id'])
    example = {}


def test_register():
    password = "password"
    res1 = api.register_user(password)
    res2 = api.register_error()
    res_body = res1.json()
    assert res1.status_code == HTTPStatus.OK
    Assert.validate_schema(res_body)
    assert res1.json()["id"] == 4
    assert res1.json()["token"] == "QpwL5tke4Pnpja7X4"
    assert res2.status_code == HTTPStatus.BAD_REQUEST

    #    Assert.validate_schema(res_body)
    assert res2.json()["error"] == "Missing password"

def test_create():
    name = 'Elena'
    job = 'la-la-la'
    res = api.create(name, job)


    assert res.status_code == HTTPStatus.CREATED
    assert res.json()['name'] == name
    assert res.json()['job'] == job
    assert re.fullmatch(r'\d{1,4}', res.json()['id'])
    assert api.delete_user(res.json()['id']).status_code == HTTPStatus.NO_CONTENT



