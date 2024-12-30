import logging
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class JSONResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            if not isinstance(response, JsonResponse):
                return response

            # Ensure consistent JSON format
            response_data = response.json()  # Will fail if not JsonResponse
            formatted_data = {
                "code": response.status_code,
                "message": "success" if response.status_code < 400 else "error",
                "data": response_data if response.status_code < 400 else None,
            }
            return JsonResponse(formatted_data, status=response.status_code)
        except Exception as e:
            logger.error(f"Error in middleware: {str(e)}")
            return JsonResponse({
                "code": 500,
                "message": f"Server error: {str(e)}",
                "data": None
            }, status=500)

class CustomExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        logger.error(f"Exception: {str(exception)}")
        return JsonResponse({
            "code": 500,
            "message": f"Exception occurred: {str(exception)}",
            "data": None
        }, status=500)
