from django.core.exceptions import ValidationError as DjangoValidationError, PermissionDenied
from django.http import Http404

from rest_framework.views import exception_handler
from rest_framework import exceptions, status
from rest_framework.serializers import as_serializer_error
from rest_framework.response import Response

from blog.exceptions import DifferentBlogAndPostError
from utils.exceptions import ApplicationError


def custom_exception_handler(exc, ctx):
    """
    {
        "message": "Error message",
        "extra": {}
    }
    """

    if isinstance(exc, DjangoValidationError):
        exc = exceptions.ValidationError(as_serializer_error(exc))

    if isinstance(exc, Http404):
        exc = exceptions.NotFound()

    if isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    response = exception_handler(exc, ctx)

    # If unexpected error occurs (server error, etc.)
    if response is None:
        if isinstance(exc, ApplicationError):

            status_code = status.HTTP_400_BAD_REQUEST

            data = {
                "message": exc.message,
                "extra": exc.extra
            }

            if isinstance(exc, DifferentBlogAndPostError):
                status_code = status.HTTP_403_FORBIDDEN

            return Response(data, status=status_code)

        return response

    if isinstance(exc.detail, (list, dict)):
        response.data = {
            "detail": response.data
        }

    if isinstance(exc, exceptions.ValidationError):
        response.data["message"] = "Validation error"
        response.data["extra"] = {
            "fields": response.data["detail"]
        }
    else:
        response.data["message"] = response.data["detail"]
        response.data["extra"] = {}

    del response.data["detail"]

    return response