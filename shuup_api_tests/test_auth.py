# -*- coding: utf-8 -*-
# This file is part of Shuup API.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import json

from rest_framework.test import APIClient
from shuup.testing.factories import get_default_shop


def test_jwt_authentication(admin_user):
    get_default_shop()
    client = APIClient()
    response = client.post("/api/api-token-auth/", data={
        "username": admin_user.username,
        "password": "password"
    })
    assert response.status_code == 200
    token = json.loads(response.content.decode("utf-8"))["token"]
    client.credentials(HTTP_AUTHORIZATION="JWT %s" % token)

    # get current user details
    response = client.get("/api/test/user/%d/" % admin_user.id)
    assert response.status_code == 200
    assert response.data["id"] == admin_user.id
    assert response.data["username"] == admin_user.username

    response = response = client.post("/api/api-token-refresh/", data={"token": token})
    assert response.status_code == 200

    client.credentials(HTTP_AUTHORIZATION='JWT bad-token')
    response = client.get("/api/test/user/")
    assert response.status_code == 401
