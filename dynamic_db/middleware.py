import re
import threading

request_cfg = threading.local()


class RouterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process the request before the view
        pattern = re.compile(r"\b(http://|https://|www\.|\.com|8000|:|//)\W*\d*", re.I)
        words = request.get_host()
        db_name = [pattern.sub("", words)][0].split('.')[0]

        request_cfg.cfg = db_name
        print("In middleware process_request:", request_cfg.cfg)

        # Call the next middleware or view
        response = self.get_response(request)

        # Process the response after the view
        if hasattr(request_cfg, 'cfg'):
            del request_cfg.cfg

        return response
