# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseBadRequest,\
                        HttpResponseNotAllowed
from django.utils import simplejson
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.db.models.query import QuerySet


def add_http_var(variable_name, required=True):
    """
    A decorators that adds the variable 'variable_name' from GET/POST
    If the variable is marked as required and not found on GET/POST,
    a HttpResponseBadRequest is returned specifying which variable is
    missing.
    """
    def wrap(func):
        def decorator(request, *args, **kwargs):
            http_var = request.REQUEST.get(variable_name, None)
            if http_var:
                kwargs[variable_name] = http_var
            elif required:
                return HttpResponseBadRequest(
                    'Please define GET or POST variable %s' % variable_name)
            else:
                pass
            return func(request, *args, **kwargs)
        return decorator
    return wrap


def json_response(func):
    """
    A decorator thats takes a view response and turns it
    into json. If a callback is added through GET or POST
    the response is JSONP.
    """
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects, HttpResponse):
            return objects
        try:
            if isinstance(objects, QuerySet):
                data = serializers.serialize("json", objects)
            else:
                data = simplejson.dumps(objects, cls=DjangoJSONEncoder)
            if 'callback' in request.REQUEST:
                # a jsonp response!
                data = '%s(%s);' % (request.REQUEST['callback'], data)
                return HttpResponse(data, "text/javascript")
        except:
            data = simplejson.dumps(str(objects), cls=DjangoJSONEncoder)
        return HttpResponse(data, "application/json")
    return decorator


def requires_post(func):
    """
    Returns an HTTP 405 error if the request method isn't POST.
    """
    def decorator(request, *args, **kwargs):
        if request.method == 'POST':
            return func(request, *args, **kwargs)
        return HttpResponseNotAllowed(['POST'])
    return decorator
