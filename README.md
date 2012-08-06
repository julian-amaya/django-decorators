django-decorators
=================
why?
----
**django-decorators** were created during many projects where I found myself rewriting over and over the same code.

Installation:
--

Simply use pip:
    
    pip install django-decorators


List of decorators:
--

#### @add_http_var
An example usage

	from django_decorators.decorators import add_http_var
	
    @add_http_var('page')
    def any_view(request, page):
        return HttpResponse(page)
        
#### @json_response

An example usage

	from django_decorators.decorators import json_response
	
    @json_response
    def any_view(request):
        return {'this will be': 'JSON'}

returns a JSON string.

Now, if you need a JSONP response, just add a callback GET or POST variable :)

#### @requires_post

An example usage

	from django_decorators.decorators import requires_post
	
    @requires_post
    def any_view(request):
        return return HttpResponse('only works with POST')




Copyright and Licensing
-----------------------

Copyright 2012 Julián Amaya M. [@julian_amaya](http://twitter.com/julian_amaya) <br />
Licensed under the Apache License, Version 2.0<br /> 
<http://www.apache.org/licenses/LICENSE-2.0>