# decorators.py
import functools
import logging

from flask import current_app, flash, jsonify, make_response, redirect, request, url_for
from flask_jwt_extended import verify_jwt_in_request
from flask_login import current_user

from .._compat import as_unicode
from ..const import (
    FLAMSG_ERR_SEC_ACCESS_DENIED,
    LOGMSG_ERR_SEC_ACCESS_DENIED,
    PERMISSION_PREFIX,
)

log = logging.getLogger(__name__)


def protect(allow_browser_login=False):

    def _protect(f):
        if hasattr(f, "_permission_name"):
            permission_str = f._permission_name
        else:
            permission_str = f.__name__

        def wraps(self, *args, **kwargs):
            permission_str = "{}{}".format(PERMISSION_PREFIX, f._permission_name)
            if self.method_permission_name:


## ... source file abbreviated to get to jsonify examples ...


    return functools.update_wrapper(wraps, f)


def has_access_api(f):
    if hasattr(f, "_permission_name"):
        permission_str = f._permission_name
    else:
        permission_str = f.__name__

    def wraps(self, *args, **kwargs):
        permission_str = "{}{}".format(PERMISSION_PREFIX, f._permission_name)
        if self.method_permission_name:
            _permission_name = self.method_permission_name.get(f.__name__)
            if _permission_name:
                permission_str = "{}{}".format(PERMISSION_PREFIX, _permission_name)
        if permission_str in self.base_permissions and self.appbuilder.sm.has_access(
            permission_str, self.class_permission_name
        ):
            return f(self, *args, **kwargs)
        else:
            log.warning(
                LOGMSG_ERR_SEC_ACCESS_DENIED.format(
                    permission_str, self.__class__.__name__
                )
            )
            response = make_response(
                jsonify(
                    {"message": str(FLAMSG_ERR_SEC_ACCESS_DENIED), "severity": "danger"}
                ),
                401,
            )
            response.headers["Content-Type"] = "application/json"
            return response

    f._permission_name = permission_str
    return functools.update_wrapper(wraps, f)


def permission_name(name):

    def wraps(f):
        f._permission_name = name
        return f

    return wraps

