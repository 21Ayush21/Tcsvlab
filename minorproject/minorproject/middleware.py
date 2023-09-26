class SimulatorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.setdefault(
            "Cross-Origin-Embedder-Policy",
            "credentialless",
        )
        response.setdefault(
            "Referrer-Policy",
            "no-referrer-when-downgrades",
        )

        return response
