# -*- coding: utf-8 -*-
# This file is part of Shuup API.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import shuup.apps


class AppConfig(shuup.apps.AppConfig):
    name = "shuup_api_test_app"
    label = "shuup_api_test_app"
    verbose_name = "Shuup API Test App"
    required_installed_apps = (
        "shuup_api",
    )

    provides = {
        "api_populator": [
            "shuup_api_test_app.api.populate_api",
        ]
    }
