from django.http import HttpRequest, HttpResponse

import datetime


def simple_middleware(get_response):
    def middleware(req: HttpRequest):
        # print
        # print(req.COOKIES)
        # print(req.session.items())
        # print(req.session.get("visited_before"), req.session.get_expire_at_browser_close())
        #
        # set cookie
        visited = int(req.COOKIES.get("visited", "0"))
        response: HttpResponse = get_response(req)

        response.set_cookie(
            "visited",
            value=f"{visited+1}",
            expires=datetime.datetime(
                2025,
                12,
                31,
                23,
                59,
                59,
                999999,
                datetime.timezone(
                    datetime.timedelta(hours=5, minutes=30),
                    "ta_IN",
                ),
            ),
            # max_age=1440,
        )

        # set session cookie

        visited_before = req.session.get("visited_before", "0")
        req.session["visited_before"] = int(visited_before) + 1
        req.session.set_expiry(0)

        return response

    return middleware


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response: HttpResponse = self.get_response(request)
        response.set_cookie(
            "ghost",
            value="busters",
            max_age=1440,
        )
        response.set_cookie(
            "tony",
            value="stink",
            max_age=1440,
        )

        # Code to be executed for each request/response after
        # the view is called.

        response["OwnerLLC"] = "Google.co.in"
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # Code to be executed for each request/response after
        # the view is called.

        # ! https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
        # ! Content Security Policy
        response["Server"] = "Apache 2.6"
        response["created-by"] = "selvaganapathi066@gmail.com"
        response["Content-Security-Policy"] = (
            """default-src 'self'; img-src 'self';script-src-elem 'self';"""
        )
        response["Content-Security-Policy-Report-Only"] = "script-src-elem"

        return response
