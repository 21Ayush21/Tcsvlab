# This file defines a custom Django middleware class `SimulatorMiddleware`. 
# The middleware is responsible for modifying the HTTP response headers to include 
# the "Cross-Origin-Embedder-Policy" with the value "require-corp". This policy 
# ensures that only resources from the same origin or those explicitly marked as 
# loadable are allowed to be embedded in the page.
# 
# The class is initialized with the `get_response` callable, which is a reference to 
# the next middleware or view in the request/response cycle.
# When the middleware is called, it processes the request, gets the response 
# from the subsequent middleware or view, and sets the "Cross-Origin-Embedder-Policy" 
# header before returning the response.

class SimulatorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.setdefault(
            "Cross-Origin-Embedder-Policy",
            "require-corp",
        )

        return response
