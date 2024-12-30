# exception_handler.py

from rest_framework.views import exception_handler
from rest_framework.exceptions import PermissionDenied

def custom_exception_handler(exc, context):
    # Call DRF's default exception handler to get the standard response
    response = exception_handler(exc, context)

    # If the exception is PermissionDenied, modify the response
    if isinstance(exc, PermissionDenied):
        response_data = {
            "code": 403,  # Forbidden error code
            "message": "You are not authorized to access this API. Please authenticate.",
            "data": None
        }
        response.data = response_data
        response.status_code = 403  # Set status code to 403 Forbidden

    # Return the modified response
    return response
