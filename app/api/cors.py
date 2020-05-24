from django import http


class CorsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        http_access = "HTTP_ACCESS_CONTROL_REQUEST_METHOD"
        methods = "DELETE, GET, OPTIONS, PATCH, POST, PUT"
        all_headers = "accept, accept-encoding, authorization, "
        all_headers_0 = "content-type, dnt, origin, user-agent, "
        all_headers_1 = "x-csrftoken, x-requested-with"
        headers = all_headers + all_headers_0 + all_headers_1
        if (request.method == "OPTIONS" and http_access in request.META):
            response = http.HttpResponse()
            response["Content-Length"] = "0"
            response["Access-Control-Max-Age"] = 86400
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = methods
        response["Access-Control-Allow-Headers"] = headers
        return response
