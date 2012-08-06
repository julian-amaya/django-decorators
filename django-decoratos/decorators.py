# -*- coding: utf-8 -*-
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseBadRequest


def json_response(func):
    """
    Use it to make a view that gives
    as a result
    """
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects, HttpResponse):
            return objects
        try:
            data = simplejson.dumps(objects)
            if 'callback' in request.GET:
                data = '%s(%s);' % (request.GET['callback'], data)
        except:
            data = simplejson.dumps(str(objects))
        if 'callback' in request.GET or 'callback' in request.POST:
            #jsonp
            return HttpResponse(data, "text/javascript")
        else:
            #json
            return HttpResponse(data, "application/json")
    return decorator


def add_http_var(variable_name, required=True):
    """
    Pasa la variable a la funcion, extrayendola del POST o GET,
    lanzando una excepcion si no existe esta y no ha sido explicitamente
    declarado opcional en True.
    """
    def wrap(func):
        def decorator(request, *args, **kwargs):
            http_var = request.REQUEST.get(variable_name, None)
            if http_var:
                kwargs[variable_name] = http_var
            elif required:
                return HttpResponseBadRequest('Please define GET or POST variable %s' % variable_name)
            else:
                pass
            return func(request, *args, **kwargs)
        return decorator
    return wrap
