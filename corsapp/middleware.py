from django.http import HttpResponse


class CorsMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        is_graphQL = True if request.path == "/graphql/" else False
        is_method_options = True if request.method == "OPTIONS" else False
        if is_graphQL and is_method_options:
            response = HttpResponse("")
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Headers"] = "*"
            response["Access-Control-Allow-Methods"] = "*"
            return response

        response = self.get_response(request)
        if is_graphQL:
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Headers"] = "*"
            response["Access-Control-Allow-Methods"] = "*"

        return response
