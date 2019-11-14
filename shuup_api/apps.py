# -*- coding: utf-8 -*-
# This file is part of Shuup API.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import shuup.apps
from django.core.exceptions import ImproperlyConfigured


class AppConfig(shuup.apps.AppConfig):
    name = "shuup_api"
    verbose_name = "Shuup API"
    label = "shuup_api"
    required_installed_apps = (
        "rest_framework",
    )

    provides = {
        "admin_module": [
            "shuup_api.admin_module:APIModule",
        ]
    }

    def ready(self):
        from django.conf import settings
        rest_framework_config = getattr(settings, "REST_FRAMEWORK", None)
        if not (rest_framework_config and rest_framework_config.get("DEFAULT_PERMISSION_CLASSES")):
            raise ImproperlyConfigured(
                "`shuup_api` REQUIRES explicit configuration of `REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES']` "
                "in your settings file. This is to avoid all of your shop's orders being world-readable-and-writable."
            )
