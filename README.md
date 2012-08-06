django-decorators
=================
why?
----
**django-decorators** were created during many projects where I found myself rewriting over and over the same code.

List of decorators:
--
#### @json_response

An example usage

    @json_response
    def any_view(request):
        return {'this will be': 'JSON'}

returns a JSON string.

Now, if you need a JSONP response, just add a callback GET or POST variable :)

#### @add_http_var
An example usage

    @add_http_var('page')
    def any_view(request, page):
        return HttpResponse(page)


Copyright and Licensing
-----------------------

Copyright 2012 Julián Amaya M.
Licensed under the Apache License, Version 2.0 
<http://www.apache.org/licenses/LICENSE-2.0>