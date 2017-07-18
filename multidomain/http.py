# coding: utf8
from django.urls import reverse_lazy


def get_domain(request, reverse_url=None, *args, **kwargs):
    """
    Create domain from django.http.request.HttpRequest.
    Optional add internal link from reverse_lazy
    :param request: Object Request
    :param reverse_url: Name urls, from project.urls.
    :param args: Optional position arguments for reverse_lazy
    :param kwargs: Optional names arguments for reverse_lazy
    :type request: django.http.request.HttpRequest
    :type reverse_url: str
    :type args: list
    :type kwargs: dict
    :return: Created link
    :rtype: str
    :raises:
    """
    url = "{}://{}".format(request.scheme, request.get_host())
    if reverse_url:
        url += str(reverse_lazy(reverse_url, args=args, kwargs=kwargs))
    return url
