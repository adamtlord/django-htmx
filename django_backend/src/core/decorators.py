from functools import wraps
from urllib.parse import urlparse, urlunparse
from django.conf import settings
from django.http import HttpResponse, QueryDict
from django.shortcuts import resolve_url
from django.contrib.auth import REDIRECT_FIELD_NAME


def htmx_login_required(view_func):
    @wraps(view_func)
    def decorator(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        path = request.build_absolute_uri()
        resolved_login_url = resolve_url(settings.LOGIN_URL)
         # If the login url is the same scheme and net location then just
        # use the path as the "next" url.
        login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
        current_scheme, current_netloc = urlparse(path)[:2]
        if (not login_scheme or login_scheme == current_scheme) and (
            not login_netloc or login_netloc == current_netloc
        ):
            path = request.get_full_path()

        login_url_parts = list(urlparse(resolved_login_url))

        querystring = QueryDict(login_url_parts[4], mutable=True)
        querystring[REDIRECT_FIELD_NAME] = path
        login_url_parts[4] = querystring.urlencode(safe="/")

        response = HttpResponse()
        response["HX-Redirect"] = urlunparse(login_url_parts)
        return response

    return decorator