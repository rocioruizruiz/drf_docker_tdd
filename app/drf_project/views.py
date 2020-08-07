# quick Django view that we can easily test.

from django.http import JsonResponse


def ping(request):
    data = {"ping": "pong"}
    return JsonResponse(data)


# Next, update urls.py in "drf_project":
