from rest_framework import exceptions, status, views


def custom_exception_handler(exc, context):
    response = views.exception_handler(exc, context)

    if isinstance(exc, (exceptions.AuthenticationFailed, exceptions.NotAuthenticated)) and response is not None:
        response.status_code = status.HTTP_401_UNAUTHORIZED

    return response
