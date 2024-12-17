from django.utils.deprecation import MiddlewareMixin


class CheckTokenTypes(MiddlewareMixin):

    def process_request(self, request):
        auth_header = request.headers.get("Authorization")
        if auth_header is None:
            return None
        elif auth_header.lower().startswith("jwt"):
            print("jwt token")
        elif auth_header.lower().startswith("bearer"):
            print("bearer token")

    def process_view(self, request, *args, **kwargs):
        pass
