from django.http import JsonResponse

def getRoutes(request):
    routes = [
        {
            'Endpoint': '/planes',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of planes'
        },
        {
            'Endpoint': '/planes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single plane'
        },
        {
            'Endpoint': '/planes/add',
            'method': 'GET',
            'body': None,
            'description': 'Adds a plane to the hangar'
        },
        {
            'Endpoint': '/planes/delete',
            'method': 'GET',
            'body': None,
            'description': 'Removes a plane from the hangar'
        },
        ]
    return JsonResponse(routes, safe=False)